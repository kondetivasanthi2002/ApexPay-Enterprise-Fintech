import pytest
from decimal import Decimal
from apps.api.credit.amortization import AmortizationEngine
from apps.api.credit.scoring import CreditScoringModel

def test_amortization_emi_calculation():
    emi = AmortizationEngine.calculate_emi(Decimal("10000.00"), Decimal("12.0"), 12)
    assert Decimal("880.00") <= emi <= Decimal("890.00")

def test_credit_scoring_algorithm():
    scorer = CreditScoringModel()
    score = scorer.calculate_score(95, 15.0, 25.0, 48)
    assert 700 <= score <= 850
