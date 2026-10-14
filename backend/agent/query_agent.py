import os
import time

from google import genai
from dotenv import load_dotenv

from logging_config import get_logger

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", "..", ".env"))

logger = get_logger(__name__)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_NAME = "gemini-3.5-flash-lite"

SCHEMA_DESCRIPTION = """
You are working with a pandas DataFrame called `df` containing bank transactions.
Columns:
- date (string, format YYYY-MM-DD)
- description (string, merchant/transaction description)
- amount (float, transaction amount)
- type (string, either "DEBIT" or "CREDIT")
- category (string, one of: Food, Travel, Shopping, Bills, Entertainment, Groceries, Salary, Rent, Other)
- is_anomaly (integer, 1 if flagged as unusual, 0 otherwise)

The DataFrame is already loaded as `df` - do not create sample data or redefine df.
`df["date"]` is already converted to pandas datetime type.
"""


def generate_pandas_code(question: str) -> str:
    """
    Asks Gemini to convert a natural language question into a single pandas expression.
    """
    prompt = f"""{SCHEMA_DESCRIPTION}

User question: "{question}"

Write a SINGLE line of pandas code that answers this question using the `df` DataFrame.
The code must assign its final answer to a variable called `result`.

Rules:
- Only use pandas operations on `df` - no other libraries, no file access, no imports.
- Do not use print(), input(), exec(), eval(), or any system/file functions.
- Keep it to ONE line of code.
- Respond with ONLY the code, no explanation, no markdown formatting, no backticks.

Example:
Question: "What is my total spending on Food?"
Code: result = df[(df["category"] == "Food") & (df["type"] == "DEBIT")]["amount"].sum()
"""

    logger.info("Gemini request -> task=pandas_code model=%s question=%r", MODEL_NAME, question)
    logger.debug("Gemini prompt: %s", prompt)

    start = time.perf_counter()
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
    except Exception as e:
        logger.error("Gemini pandas_code failed for %r: %s", question, e)
        raise
    elapsed = time.perf_counter() - start

    code = response.text.strip()
    code = code.replace("```python", "").replace("```", "").strip()

    logger.info("Gemini response <- task=pandas_code code=%r latency=%.3fs", code, elapsed)
    return code


def explain_result(question: str, result) -> str:
    """
    Asks Gemini to turn a raw result into a natural language answer.
    """
    prompt = f"""A user asked: "{question}"

The computed answer is: {result}

Write ONE short, natural sentence answering the user's question using this result.
Format any money values with the Rupee symbol and commas (e.g. Rs. 12,450.00).
Do not explain how the calculation was done - just state the answer clearly."""

    logger.info("Gemini request -> task=explain model=%s question=%r", MODEL_NAME, question)
    logger.debug("Gemini prompt: %s", prompt)

    start = time.perf_counter()
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
    except Exception as e:
        logger.error("Gemini explain failed for %r: %s", question, e)
        raise
    elapsed = time.perf_counter() - start

    answer = response.text.strip()

    logger.info("Gemini response <- task=explain answer=%r latency=%.3fs", answer, elapsed)
    return answer