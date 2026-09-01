from fastapi import APIRouter, HTTPException
from decimal import Decimal
from packages.ledger_core.engine import DoubleEntryEngine
from packages.ledger_core.models import AccountType, JournalEntry

router = APIRouter(prefix="/api/v1/ledger", tags=["Ledger Engine"])
ledger_engine = DoubleEntryEngine()

# Seed default accounts
ledger_engine.create_account("ACC-1001", "1010", "Operating Cash", AccountType.ASSET)
ledger_engine.create_account("ACC-2001", "2010", "Customer Deposits", AccountType.LIABILITY)
ledger_engine.create_account("ACC-4001", "4010", "Processing Fee Income", AccountType.REVENUE)

@router.get("/accounts")
def list_accounts():
    return [acc.dict() for acc in ledger_engine.accounts.values()]

@router.post("/post")
def post_journal_entry(entry: JournalEntry):
    try:
        ledger_engine.post_entry(entry)
        return {"status": "SUCCESS", "entry_id": entry.entry_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/verify")
def verify_ledger():
    valid = ledger_engine.verify_ledger_invariants()
    return {"ledger_valid": valid, "account_count": len(ledger_engine.accounts)}
