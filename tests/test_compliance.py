import pytest
from decimal import Decimal
from apps.api.compliance.sanctions import SanctionScreeningEngine
from apps.api.compliance.transaction_monitoring import TransactionMonitoringEngine

def test_sanction_screening_hit():
    engine = SanctionScreeningEngine()
    res = engine.screen_entity("VIKTOR BOUT")
    assert res["flagged"] is True

def test_sanction_screening_clean():
    engine = SanctionScreeningEngine()
    res = engine.screen_entity("JOHN SMITH")
    assert res["flagged"] is False

def test_transaction_monitoring_structuring():
    engine = TransactionMonitoringEngine()
    res = engine.evaluate_transaction(Decimal("12000.00"), [])
    assert "CTR_TRIGGER_THRESHOLD_EXCEEDED" in res["triggered_rules"]
