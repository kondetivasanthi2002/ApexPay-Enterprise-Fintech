from fastapi import FastAPI
from apps.api.ledger.routes import router as ledger_router
from apps.api.payments.routes import router as payments_router
from apps.api.compliance.routes import router as compliance_router
from apps.api.credit.routes import router as credit_router
from apps.api.trading.routes import router as trading_router
from apps.api.reporting.routes import router as reporting_router

app = FastAPI(
    title="ApexPay Enterprise Fintech Platform API",
    description="High-performance Double-Entry Ledger, Payment Processing Gateway, Compliance Engine, and Trading API.",
    version="1.0.0"
)

app.include_router(ledger_router)
app.include_router(payments_router)
app.include_router(compliance_router)
app.include_router(credit_router)
app.include_router(trading_router)
app.include_router(reporting_router)

@app.get("/")
def root_health():
    return {"status": "ONLINE", "system": "ApexPay Enterprise Fintech Core", "version": "1.0.0"}
