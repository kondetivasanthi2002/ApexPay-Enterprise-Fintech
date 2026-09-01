import csv
import io
from typing import List, Dict

class ReportExporter:
    @staticmethod
    def export_accounts_to_csv(accounts: List[Dict[str, any]]) -> str:
        output = io.StringIO()
        fieldnames = ["account_id", "name", "account_type", "balance", "currency"]
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        for acc in accounts:
            writer.writerow({
                "account_id": acc.get("account_id"),
                "name": acc.get("name"),
                "account_type": acc.get("account_type"),
                "balance": str(acc.get("balance")),
                "currency": acc.get("currency", "USD")
            })
        return output.getvalue()
