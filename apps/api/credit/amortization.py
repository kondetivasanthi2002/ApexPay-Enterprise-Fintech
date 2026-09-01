from decimal import Decimal
from typing import List, Dict

class AmortizationEngine:
    @staticmethod
    def calculate_emi(principal: Decimal, annual_rate_pct: Decimal, tenure_months: int) -> Decimal:
        monthly_rate = (annual_rate_pct / Decimal("100.0")) / Decimal("12.0")
        if monthly_rate == 0:
            return round(principal / Decimal(tenure_months), 2)
        
        compound_factor = (Decimal("1.0") + monthly_rate) ** tenure_months
        emi = principal * monthly_rate * compound_factor / (compound_factor - Decimal("1.0"))
        return round(emi, 2)

    @staticmethod
    def generate_schedule(principal: Decimal, annual_rate_pct: Decimal, tenure_months: int) -> List[Dict[str, str]]:
        monthly_rate = (annual_rate_pct / Decimal("100.0")) / Decimal("12.0")
        emi = AmortizationEngine.calculate_emi(principal, annual_rate_pct, tenure_months)
        
        balance = principal
        schedule = []
        for month in range(1, tenure_months + 1):
            interest_payment = round(balance * monthly_rate, 2)
            principal_payment = emi - interest_payment
            balance = round(balance - principal_payment, 2)

            schedule.append({
                "month": month,
                "emi": str(emi),
                "principal_paid": str(principal_payment),
                "interest_paid": str(interest_payment),
                "remaining_balance": str(max(Decimal("0.00"), balance))
            })
        return schedule
