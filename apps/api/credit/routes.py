from fastapi import APIRouter
from decimal import Decimal
from apps.api.credit.amortization import AmortizationEngine

router = APIRouter(prefix="/api/v1/credit", tags=["Credit & Loans"])

@router.get("/amortize")
def get_amortization_schedule(principal: float, annual_rate: float, months: int):
    return AmortizationEngine.generate_schedule(Decimal(str(principal)), Decimal(str(annual_rate)), months)
