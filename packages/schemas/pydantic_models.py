from pydantic import BaseModel, Field
from typing import List, Optional
from decimal import Decimal

class UserProfileSchema(BaseModel):
    user_id: str
    email: str
    first_name: str
    last_name: str
    kyc_status: str = "PENDING"
    risk_rating: str = "LOW"

class AccountStatementSchema(BaseModel):
    account_id: str
    opening_balance: Decimal
    closing_balance: Decimal
    total_debits: Decimal
    total_credits: Decimal
    statement_period: str

class FinancialReportSchema(BaseModel):
    report_name: str
    as_of_date: str
    currency: str = "USD"
    items: List[dict]
    total_amount: Decimal
