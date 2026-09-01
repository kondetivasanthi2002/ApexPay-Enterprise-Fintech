from decimal import Decimal
from typing import Dict

class CreditScoringModel:
    def calculate_score(self, payment_history_score: int, utilization_pct: float, dti_pct: float, credit_age_months: int) -> int:
        # FICO-style weighted credit scoring model (Range 300 - 850)
        base_score = 300
        
        # Payment History (35% weight -> max 192 pts)
        pay_pts = min(192, int((payment_history_score / 100.0) * 192))

        # Credit Utilization (30% weight -> max 165 pts)
        if utilization_pct <= 10: util_pts = 165
        elif utilization_pct <= 30: util_pts = 140
        elif utilization_pct <= 50: util_pts = 90
        else: util_pts = 30

        # Credit History Age (15% weight -> max 82 pts)
        age_pts = min(82, int((credit_age_months / 120.0) * 82))

        # Debt-to-Income Ratio (20% weight -> max 111 pts)
        if dti_pct <= 20: dti_pts = 111
        elif dti_pct <= 36: dti_pts = 85
        elif dti_pct <= 50: dti_pts = 40
        else: dti_pts = 10

        total_score = base_score + pay_pts + util_pts + age_pts + dti_pts
        return min(850, max(300, total_score))
