from fastapi import FastAPI
from database import engine, Base
import models
from routers import transactions, categorization, anomaly, analysis, agent

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SpendWise AI Backend")

app.include_router(transactions.router)
app.include_router(categorization.router)
app.include_router(anomaly.router)
app.include_router(analysis.router)
app.include_router(agent.router)
@app.get("/")
def read_root():
    return {"message": "SpendWise AI backend is running"}