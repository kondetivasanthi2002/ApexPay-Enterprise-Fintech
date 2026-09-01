from decimal import Decimal
from typing import Dict
from apps.api.credit.scoring import CreditScoringModel

class UnderwritingEngine:
    def __init__(self):
        self.scorer = CreditScoringModel()

    def evaluate_loan_application(self, requested_amount: Decimal, annual_income: Decimal, score: int) -> Dict[str, any]:
        dti_max = Decimal("0.45")
        max_loan_ratio = Decimal("0.40")

        approved = False
        reason = ""

        if score < 620:
            reason = "Credit score below minimum underwriting threshold (620)"
        elif requested_amount > (annual_income * max_loan_ratio):
            reason = "Requested loan amount exceeds income capacity ratio"
        else:
            approved = True
            reason = "Loan approved under standard prime tier guidelines"

        return {
            "approved": approved,
            "credit_score": score,
            "max_approved_amount": str(annual_income * max_loan_ratio),
            "decision_reason": reason
        }
