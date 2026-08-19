from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
from datetime import datetime

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    description = Column(String)
    amount = Column(Float)
    type = Column(String)          # DEBIT or CREDIT
    category = Column(String, nullable=True)          # filled in later by categorization
    category_source = Column(String, nullable=True)   # "rule", "ml", or "llm"
    is_anomaly = Column(Integer, default=0)            # 0 = normal, 1 = flagged
    created_at = Column(DateTime, default=datetime.utcnow)

