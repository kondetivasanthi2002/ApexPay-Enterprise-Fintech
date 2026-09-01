from enum import Enum
from datetime import datetime
from typing import List, Optional
from decimal import Decimal
from pydantic import BaseModel, Field

class AccountType(str, Enum):
    ASSET = "ASSET"
    LIABILITY = "LIABILITY"
    EQUITY = "EQUITY"
    REVENUE = "REVENUE"
    EXPENSE = "EXPENSE"

class EntryType(str, Enum):
    DEBIT = "DEBIT"
    CREDIT = "CREDIT"

class Account(BaseModel):
    account_id: str
    account_number: str
    name: str
    account_type: AccountType
    currency: str = "USD"
    balance: Decimal = Decimal("0.00")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True

class Posting(BaseModel):
    posting_id: str
    account_id: str
    entry_type: EntryType
    amount: Decimal
    currency: str = "USD"
    description: str

class JournalEntry(BaseModel):
    entry_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    reference: str
    description: str
    postings: List[Posting]
    checksum: str = ""
    status: str = "POSTED"
