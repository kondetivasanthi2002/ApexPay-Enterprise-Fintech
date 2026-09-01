from decimal import Decimal
from typing import Dict, List
from packages.ledger_core.models import Account, JournalEntry, EntryType, AccountType

class DoubleEntryEngine:
    def __init__(self):
        self.accounts: Dict[str, Account] = {}
        self.journal: List[JournalEntry] = []

    def create_account(self, account_id: str, account_number: str, name: str, account_type: AccountType, currency: str = "USD") -> Account:
        if account_id in self.accounts:
            raise ValueError(f"Account {account_id} already exists")
        account = Account(account_id=account_id, account_number=account_number, name=name, account_type=account_type, currency=currency)
        self.accounts[account_id] = account
        return account

    def post_entry(self, entry: JournalEntry) -> bool:
        # Check double-entry zero sum invariant
        total_debits = sum(p.amount for p in entry.postings if p.entry_type == EntryType.DEBIT)
        total_credits = sum(p.amount for p in entry.postings if p.entry_type == EntryType.CREDIT)

        if total_debits != total_credits:
            raise ValueError(f"Double-entry violation: Debits ({total_debits}) != Credits ({total_credits})")

        # Verify all accounts exist
        for posting in entry.postings:
            if posting.account_id not in self.accounts:
                raise ValueError(f"Account {posting.account_id} not found")

        # Update account balances according to fundamental accounting equation
        for posting in entry.postings:
            acc = self.accounts[posting.account_id]
            if acc.account_type in (AccountType.ASSET, AccountType.EXPENSE):
                if posting.entry_type == EntryType.DEBIT:
                    acc.balance += posting.amount
                else:
                    acc.balance -= posting.amount
            else:
                if posting.entry_type == EntryType.CREDIT:
                    acc.balance += posting.amount
                else:
                    acc.balance -= posting.amount

        self.journal.append(entry)
        return True

    def verify_ledger_invariants(self) -> bool:
        # Fundamental Accounting Equation: Assets = Liabilities + Equity + (Revenue - Expenses)
        assets = sum(a.balance for a in self.accounts.values() if a.account_type == AccountType.ASSET)
        liabilities = sum(a.balance for a in self.accounts.values() if a.account_type == AccountType.LIABILITY)
        equity = sum(a.balance for a in self.accounts.values() if a.account_type == AccountType.EQUITY)
        revenue = sum(a.balance for a in self.accounts.values() if a.account_type == AccountType.REVENUE)
        expenses = sum(a.balance for a in self.accounts.values() if a.account_type == AccountType.EXPENSE)

        net_equity = equity + (revenue - expenses)
        return assets == (liabilities + net_equity)
