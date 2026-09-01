import pytest
from apps.api.reporting.exporters import ReportExporter

def test_csv_exporter():
    sample_accounts = [
        {"account_id": "A101", "name": "Cash", "account_type": "ASSET", "balance": "5000.00", "currency": "USD"},
        {"account_id": "L201", "name": "Payables", "account_type": "LIABILITY", "balance": "1200.00", "currency": "USD"}
    ]
    csv_str = ReportExporter.export_accounts_to_csv(sample_accounts)
    assert "account_id,name,account_type,balance,currency" in csv_str
    assert "A101,Cash,ASSET,5000.00,USD" in csv_str
