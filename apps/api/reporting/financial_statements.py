from decimal import Decimal
from typing import Dict, List

class FinancialStatementGenerator:
    @staticmethod
    def generate_balance_sheet(accounts_data: List[dict]) -> Dict[str, any]:
        assets = [a for a in accounts_data if a["account_type"] == "ASSET"]
        liabilities = [a for a in accounts_data if a["account_type"] == "LIABILITY"]
        equity = [a for a in accounts_data if a["account_type"] == "EQUITY"]

        total_assets = sum(Decimal(a["balance"]) for a in assets)
        total_liabilities = sum(Decimal(a["balance"]) for a in liabilities)
        total_equity = sum(Decimal(a["balance"]) for a in equity)

        return {
            "title": "Consolidated Balance Sheet",
            "total_assets": str(total_assets),
            "total_liabilities": str(total_liabilities),
            "total_equity": str(total_equity),
            "is_balanced": total_assets == (total_liabilities + total_equity)
        }
