import pytest
from apps.api.credit.esg_scoring import ESGRiskEngine

def test_esg_risk_score_calculation():
    engine = ESGRiskEngine()
    res = engine.calculate_esg_score(carbon_intensity_g_per_dollar=50.0, board_diversity_pct=40.0, data_privacy_compliance=True)
    assert res["environmental"] == 90
    assert res["social"] == 80
    assert res["governance"] == 100
    assert res["esg_rating"] == "AAA"
