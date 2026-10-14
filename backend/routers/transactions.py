import csv
import io
import os
import re
from typing import List, Dict, Any, Optional, Tuple
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import pandas as pd

from database import get_db
from models import Transaction
from routers.categorization import retrain_ml_model
from logging_config import get_logger

logger = get_logger(__name__)

router = APIRouter(prefix="/transactions", tags=["transactions"])


def decode_file_contents(contents: bytes) -> str:
    """
    Attempts to decode file contents using common encodings,
    including utf-8 with BOM (Excel CSV export), standard utf-8, latin-1, and cp1252.
    """
    for enc in ["utf-8-sig", "utf-8", "latin-1", "cp1252"]:
        try:
            return contents.decode(enc)
        except UnicodeDecodeError:
            continue
    return contents.decode("utf-8", errors="ignore")


def clean_amount(val: Any) -> float:
    """
    Robustly parses monetary amounts from various CSV formats:
    - Currency symbols (₹, $, €, £, Rs., INR, USD)
    - Comma formats (1,250.50, 1,00,000.00)
    - Accounting parentheses: (450.00) -> -450.00
    - Whitespace and stray symbols
    """
    if val is None:
        return 0.0
    val_str = str(val).strip()
    if not val_str:
        return 0.0

    # Check for accounting negative notation: (123.45)
    is_neg = False
    if "(" in val_str and ")" in val_str:
        is_neg = True
        val_str = val_str.replace("(", "").replace(")", "")

    # Strip currency letters/symbols while retaining digits, periods, commas, minus
    cleaned = re.sub(r"[^\d.,\-+]", "", val_str)
    # Extract number pattern
    m = re.search(r"[-+]?\s*(?:\d{1,3}(?:,\d{2,3})+|\d+)(?:\.\d+)?", cleaned)
    if not m:
        return 0.0

    clean_num = m.group(0).replace(",", "").replace(" ", "")
    try:
        parsed = float(clean_num)
        return -abs(parsed) if is_neg else parsed
    except ValueError:
        return 0.0


def normalize_date(val: Any) -> str:
    """
    Converts diverse date formats (DD/MM/YYYY, MM/DD/YYYY, YYYY-MM-DD, DD-Mon-YYYY)
    into standard YYYY-MM-DD for reliable SQL queries and analytics.
    """
    s = str(val).strip()
    if not s:
        return pd.Timestamp.today().strftime("%Y-%m-%d")

    try:
        dt = pd.to_datetime(s, dayfirst=True)
        return dt.strftime("%Y-%m-%d")
    except Exception:
        try:
            dt = pd.to_datetime(s, dayfirst=False)
            return dt.strftime("%Y-%m-%d")
        except Exception:
            # Fallback: keep alphanumeric date representation
            return s[:10]


def map_columns(headers: List[str]) -> Tuple[Dict[str, Optional[str]], List[str]]:
    """
    Auto-detects and maps common alternate column headers from bank statements
    to SpendWise AI's expected schema:
    - date: Date, Txn Date, Transaction Date, Value Date, Posting Date
    - description: Description, Narration, Particulars, Details, Merchant, Payee, Remarks
    - amount: Amount, Txn Amount, Value, Net Amount
    - type: Type, Txn Type, Dr/Cr, Debit/Credit
    - debit: Debit, Debit Amount, Withdrawal, Withdrawal Amount, Dr, Paid Out
    - credit: Credit, Credit Amount, Deposit, Deposit Amount, Cr, Paid In
    """
    def norm(h: str) -> str:
        # Strip parenthetical annotations like '(INR)', '(DD/MM/YYYY)'
        clean = re.sub(r"\(.*?\)", "", h)
        return re.sub(r"[^a-z0-9]", "", clean.lower().strip())

    date_synonyms = [
        "date", "txndate", "transactiondate", "transdate", "purchasedate",
        "orderdate", "valuedate", "postingdate", "postdate", "bookingdate"
    ]
    desc_synonyms = [
        "description", "desc", "narration", "particulars", "details",
        "merchant", "merchantname", "payee", "remarks", "transactiondetails",
        "txnremarks", "memo", "notes", "product", "products", "productinformation",
        "productinfo", "productname", "productdescription", "productdetails",
        "item", "items", "itemname", "itemdescription", "orderinfo", "orderdetails", "title"
    ]
    debit_synonyms = [
        "debit", "debits", "debitamount", "debitamt", "withdrawal",
        "withdrawalamount", "withdrawalamt", "withdrawals", "dr",
        "dramount", "paidout", "expense", "spent"
    ]
    credit_synonyms = [
        "credit", "credits", "creditamount", "creditamt", "deposit",
        "depositamount", "depositamt", "deposits", "cr", "cramount",
        "paidin", "income", "received"
    ]
    amt_synonyms = [
        "amount", "amt", "transactionamount", "txnamount",
        "netamount", "totalamount", "value", "transamount"
    ]
    type_synonyms = [
        "type", "txntype", "transactiontype", "transtype",
        "drcr", "crdr", "debitcredit", "creditdebit", "dc", "entrytype"
    ]
    location_synonyms = [
        "location", "city", "store", "branch", "country", "region"
    ]

    date_col, desc_col, amt_col, type_col, debit_col, credit_col, loc_col = None, None, None, None, None, None, None

    # Pass 1: Exact normalized matches
    for h in headers:
        nh = norm(h)
        if not date_col and nh in date_synonyms:
            date_col = h
        elif not desc_col and nh in desc_synonyms:
            desc_col = h
        elif not debit_col and nh in debit_synonyms:
            debit_col = h
        elif not credit_col and nh in credit_synonyms:
            credit_col = h
        elif not type_col and nh in type_synonyms:
            type_col = h
        elif not amt_col and nh in amt_synonyms:
            amt_col = h
        elif not loc_col and nh in location_synonyms:
            loc_col = h

    # Pass 2: Substring heuristics for unmapped fields
    for h in headers:
        nh = norm(h)
        # Match 'date' but exclude customer metadata like 'signup_date', 'birth_date', 'expiry_date'
        if not date_col and "date" in nh and not any(x in nh for x in ["signup", "birth", "expiry", "due", "created"]):
            date_col = h
        if not desc_col and any(x in nh for x in ["narration", "particular", "merchant", "desc", "detail", "remark", "product", "item", "order"]):
            desc_col = h
        if not debit_col and any(x in nh for x in ["withdraw", "debit"]):
            debit_col = h
        if not credit_col and any(x in nh for x in ["deposit", "credit"]):
            credit_col = h
        if not amt_col and not (debit_col or credit_col) and ("amount" in nh or "amt" in nh):
            amt_col = h
        if not loc_col and any(x in nh for x in ["location", "city", "store"]):
            loc_col = h

    mapping = {
        "date": date_col,
        "description": desc_col,
        "amount": amt_col,
        "type": type_col,
        "debit": debit_col,
        "credit": credit_col,
        "location": loc_col
    }

    missing = []
    if not date_col:
        missing.append("Date (e.g. 'date', 'transaction_date', 'txn_date', 'value_date')")
    if not desc_col:
        missing.append("Description (e.g. 'description', 'narration', 'particulars', 'merchant', 'details')")
    if not amt_col and not (debit_col or credit_col):
        missing.append("Amount (e.g. 'amount', 'amt', or separate 'Debit'/'Withdrawal' & 'Credit'/'Deposit' columns)")

    return mapping, missing


@router.post("/upload")
async def upload_transactions(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    Robust transaction CSV upload:
    - Auto-detects and maps alternate column headers (case-insensitive, synonyms)
    - Supports unified Amount column or dual Debit/Credit columns
    - Parses currencies, comma separators, accounting negatives
    - Validates data BEFORE clearing existing records (atomic update)
    - Returns detailed 400 error listing missing vs detected columns if mapping fails
    """
    logger.info("Upload request received for file: %r", file.filename)

    try:
        contents = await file.read()
    except Exception as e:
        logger.error("Failed to read uploaded file: %s", e)
        raise HTTPException(status_code=400, detail=f"Could not read uploaded file: {str(e)}")

    if not contents or len(contents.strip()) == 0:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Empty file",
                "message": "The uploaded CSV file is empty.",
                "suggestion": "Please upload a valid CSV bank statement containing transaction rows."
            }
        )

    decoded = decode_file_contents(contents)
    csv_file = io.StringIO(decoded)

    try:
        # Sniff delimiter (handles comma, semicolon, tab)
        sample = decoded[:2048]
        delimiter = ","
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",\t;|")
            delimiter = dialect.delimiter
        except Exception:
            delimiter = ","

        csv_file.seek(0)
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        raw_headers = reader.fieldnames or []
    except Exception as e:
        logger.error("Failed to parse CSV structure: %s", e)
        raise HTTPException(
            status_code=400,
            detail={
                "error": "CSV Parse Error",
                "message": f"Could not parse the uploaded file as a CSV: {str(e)}",
                "suggestion": "Please ensure the file is a properly formatted CSV text file."
            }
        )

    if not raw_headers:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Missing Headers",
                "message": "No column headers detected in the uploaded CSV file.",
                "suggestion": "Please ensure the first row of your CSV contains column names."
            }
        )

    # Auto-detect and map columns
    mapping, missing = map_columns(raw_headers)

    if missing:
        logger.warning(
            "CSV column mapping failed for %r. Detected: %s, Missing: %s",
            file.filename, raw_headers, missing
        )
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Column mapping failed",
                "message": "The uploaded CSV could not be recognized as a financial statement.",
                "missing_required_fields": missing,
                "detected_headers": raw_headers,
                "suggestion": (
                    "SpendWise AI requires transaction records with Date, Description, and Amount "
                    "(or separate Debit/Credit columns). Non-financial files (e.g. customer lists, "
                    "product catalogs) cannot be processed."
                )
            }
        )

    date_key = mapping["date"]
    desc_key = mapping["description"]
    amt_key = mapping["amount"]
    type_key = mapping["type"]
    debit_key = mapping["debit"]
    credit_key = mapping["credit"]
    loc_key = mapping.get("location")

    logger.info("Mapped columns for %r: %s", file.filename, mapping)

    # First pass: parse all rows in memory without modifying the database
    transactions_to_add = []
    skipped_rows = 0

    for row_num, row in enumerate(reader, start=2):
        # Skip completely empty rows
        if not row or not any(str(v).strip() for v in row.values() if v is not None):
            continue

        date_val = normalize_date(row.get(date_key))
        desc_val = str(row.get(desc_key) or "").strip()
        if loc_key and row.get(loc_key):
            loc_val = str(row.get(loc_key)).strip()
            if loc_val and loc_val.lower() not in desc_val.lower():
                desc_val = f"{desc_val} ({loc_val})"
        if not desc_val:
            desc_val = "Unspecified Transaction"

        amount = 0.0
        txn_type = "DEBIT"

        # Case A: Separate Debit and Credit columns exist
        if debit_key or credit_key:
            debit_amt = clean_amount(row.get(debit_key)) if debit_key else 0.0
            credit_amt = clean_amount(row.get(credit_key)) if credit_key else 0.0

            if abs(debit_amt) > 0 and abs(credit_amt) == 0:
                amount = abs(debit_amt)
                txn_type = "DEBIT"
            elif abs(credit_amt) > 0 and abs(debit_amt) == 0:
                amount = abs(credit_amt)
                txn_type = "CREDIT"
            elif abs(debit_amt) > 0 and abs(credit_amt) > 0:
                if abs(credit_amt) > abs(debit_amt):
                    amount = abs(credit_amt) - abs(debit_amt)
                    txn_type = "CREDIT"
                else:
                    amount = abs(debit_amt) - abs(credit_amt)
                    txn_type = "DEBIT"
            elif amt_key:
                # Fallback to amount column if both debit & credit cells are 0/empty
                raw_amt = clean_amount(row.get(amt_key))
                amount = abs(raw_amt)
                txn_type = "DEBIT" if raw_amt < 0 else "CREDIT"
            else:
                skipped_rows += 1
                continue

        # Case B: Single unified Amount column
        elif amt_key:
            raw_amt = clean_amount(row.get(amt_key))
            amount = abs(raw_amt)

            # Determine type from Type column if available
            if type_key and row.get(type_key):
                raw_type = str(row.get(type_key)).strip().upper()
                if any(x in raw_type for x in ["CR", "CREDIT", "DEP", "INCOME", "INFLOW", "+"]):
                    txn_type = "CREDIT"
                elif any(x in raw_type for x in ["DR", "DEBIT", "WDL", "EXPENSE", "OUTFLOW", "PAYMENT", "-"]):
                    txn_type = "DEBIT"
                else:
                    txn_type = "DEBIT" if raw_amt < 0 else "CREDIT" if raw_amt > 0 else "DEBIT"
            else:
                # Infer from sign of amount or description keywords
                if raw_amt < 0:
                    txn_type = "DEBIT"
                elif any(kw in desc_val.lower() for kw in ["salary", "deposit", "refund", "interest credited", "cashback"]):
                    txn_type = "CREDIT"
                else:
                    txn_type = "DEBIT"

        if amount == 0.0 and (not desc_val or desc_val == "Unspecified Transaction"):
            skipped_rows += 1
            continue

        transaction = Transaction(
            date=date_val,
            description=desc_val,
            amount=round(amount, 2),
            type=txn_type,
        )
        transactions_to_add.append(transaction)

    if not transactions_to_add:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "No valid transactions",
                "message": "The CSV was read, but no valid transaction rows containing amounts could be parsed.",
                "suggestion": "Please ensure the CSV rows have valid non-zero amounts."
            }
        )

    # Validation succeeded: Now perform atomic database replacement
    logger.info("Clearing old transactions and inserting %d validated transactions", len(transactions_to_add))
    db.query(Transaction).delete()
    for txn in transactions_to_add:
        db.add(txn)
    db.commit()

    # Clear previously trained ML model since new data is loaded
    model_dir = os.path.join(os.path.dirname(__file__), "..", "categorization")
    for filename in ["ml_model.joblib", "vectorizer.joblib"]:
        filepath = os.path.join(model_dir, filename)
        if os.path.exists(filepath):
            try:
                os.remove(filepath)
            except Exception as e:
                logger.warning("Could not remove model file %s: %s", filename, e)

    # Reset RAG service instance so it syncs new transactions immediately
    try:
        from agent.rag_service import FinancialRAGService
        FinancialRAGService._instance = None
    except Exception:
        pass

    logger.info("Upload complete: %d transactions inserted successfully", len(transactions_to_add))
    return {
        "message": f"Uploaded {len(transactions_to_add)} transactions successfully (previous data and model cleared)",
        "count": len(transactions_to_add),
        "mapped_columns": {k: v for k, v in mapping.items() if v is not None},
        "skipped_rows": skipped_rows
    }


@router.get("/")
def list_transactions(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()
    return transactions


class CorrectionRequest(BaseModel):
    category: str


@router.patch("/{transaction_id}/correct")
def correct_transaction(transaction_id: int, request: CorrectionRequest, db: Session = Depends(get_db)):
    txn = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not txn:
        return {"error": f"Transaction {transaction_id} not found"}

    txn.category = request.category
    txn.category_source = "human"
    db.commit()

    retrain_result = retrain_ml_model(db)

    return {
        "message": f"Transaction {transaction_id} updated",
        "id": txn.id,
        "new_category": txn.category,
        "retrain_result": retrain_result,
    }