from fastapi import APIRouter
from apps.api.compliance.sanctions import SanctionScreeningEngine
from apps.api.compliance.transaction_monitoring import TransactionMonitoringEngine

router = APIRouter(prefix="/api/v1/compliance", tags=["KYC & Compliance"])
sanctions_engine = SanctionScreeningEngine()
monitoring_engine = TransactionMonitoringEngine()

@router.post("/screen")
def screen_entity(name: str):
    return sanctions_engine.screen_entity(name)
