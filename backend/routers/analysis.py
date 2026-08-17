from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from analysis.trends import get_monthly_category_spending, get_month_over_month_change, get_affordability_analysis

router = APIRouter(prefix="/analysis", tags=["analysis"])


@router.get("/monthly-category")
def monthly_category_spending(db: Session = Depends(get_db)):
    return get_monthly_category_spending(db)


@router.get("/monthly-trend")
def monthly_trend(db: Session = Depends(get_db)):
    return get_month_over_month_change(db)



@router.get("/affordability")
def affordability(purchase_amount: float, db: Session = Depends(get_db)):
    return get_affordability_analysis(db, purchase_amount)