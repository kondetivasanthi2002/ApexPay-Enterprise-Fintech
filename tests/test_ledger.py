import pytest
from decimal import Decimal
from packages.ledger_core.engine import DoubleEntryEngine
from packages.ledger_core.models import AccountType, JournalEntry, Posting, EntryType
from packages.ledger_core.forex import CurrencyConverter
from packages.ledger_core.checksum import LedgerAuditChecksum

def test_double_entry_balance_equation():
    engine = DoubleEntryEngine()
    engine.create_account("A1", "100", "Cash", AccountType.ASSET)
    engine.create_account("L1", "200", "Deposit", AccountType.LIABILITY)

    entry = JournalEntry(
        entry_id="E-1",
        reference="REF-001",
        description="Customer Deposit",
        postings=[
            Posting(posting_id="P1", account_id="A1", entry_type=EntryType.DEBIT, amount=Decimal("500.00"), description="Cash in"),
            Posting(posting_id="P2", account_id="L1", entry_type=EntryType.CREDIT, amount=Decimal("500.00"), description="Liability recognized")
        ]
    )

    assert engine.post_entry(entry) is True
    assert engine.accounts["A1"].balance == Decimal("500.00")
    assert engine.accounts["L1"].balance == Decimal("500.00")
    assert engine.verify_ledger_invariants() is True

def test_double_entry_imbalance_raises_error():
    engine = DoubleEntryEngine()
    engine.create_account("A1", "100", "Cash", AccountType.ASSET)
    engine.create_account("L1", "200", "Deposit", AccountType.LIABILITY)

    bad_entry = JournalEntry(
        entry_id="E-2",
        reference="REF-002",
        description="Imbalanced Entry",
        postings=[
            Posting(posting_id="P1", account_id="A1", entry_type=EntryType.DEBIT, amount=Decimal("500.00"), description="Cash in"),
            Posting(posting_id="P2", account_id="L1", entry_type=EntryType.CREDIT, amount=Decimal("400.00"), description="Bad credit")
        ]
    )

    with pytest.raises(ValueError):
        engine.post_entry(bad_entry)

def test_currency_conversion():
    converter = CurrencyConverter()
    converted = converter.convert(Decimal("100.00"), "EUR", "USD")
    assert converted > Decimal("100.00")

def test_ledger_checksum_audit():
    entry_data = {"entry_id": "E-100", "timestamp": "2026-09-01T20:00:00", "reference": "REF1", "postings": []}
    h1 = LedgerAuditChecksum.compute_entry_hash(entry_data, "GENESIS")
    assert len(h1) == 64
