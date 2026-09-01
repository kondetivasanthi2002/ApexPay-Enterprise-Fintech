from fastapi import APIRouter
from apps.api.reporting.financial_statements import FinancialStatementGenerator

router = APIRouter(prefix="/api/v1/reporting", tags=["Financial Statements"])

@router.get("/balance-sheet")
def get_balance_sheet():
    sample_accounts = [
        {"account_type": "ASSET", "balance": "150000.00"},
        {"account_type": "LIABILITY", "balance": "50000.00"},
        {"account_type": "EQUITY", "balance": "100000.00"}
    ]
    return FinancialStatementGenerator.generate_balance_sheet(sample_accounts)
