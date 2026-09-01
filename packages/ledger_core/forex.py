from decimal import Decimal
from typing import Dict

class CurrencyConverter:
    def __init__(self):
        # Default exchange rates relative to USD
        self.rates: Dict[str, Decimal] = {
            "USD": Decimal("1.0000"),
            "EUR": Decimal("1.0850"),
            "GBP": Decimal("1.2700"),
            "JPY": Decimal("0.0067"),
            "CAD": Decimal("0.7400"),
            "AUD": Decimal("0.6500"),
            "CHF": Decimal("1.1200")
        }

    def convert(self, amount: Decimal, from_curr: str, to_curr: str) -> Decimal:
        if from_curr not in self.rates or to_curr not in self.rates:
            raise ValueError(f"Unsupported currency pair: {from_curr}/{to_curr}")
        usd_val = amount * self.rates[from_curr]
        return round(usd_val / self.rates[to_curr], 4)

    def revaluate_portfolio(self, balances: Dict[str, Decimal], target_curr: str = "USD") -> Decimal:
        total = Decimal("0.00")
        for curr, amount in balances.items():
            total += self.convert(amount, curr, target_curr)
        return total
