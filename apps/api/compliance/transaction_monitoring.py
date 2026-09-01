from decimal import Decimal
from typing import List, Dict

class TransactionMonitoringEngine:
    def __init__(self):
        self.structuring_threshold = Decimal("10000.00")
        self.micro_tx_limit = Decimal("9500.00")

    def evaluate_transaction(self, amount: Decimal, recent_history: List[Decimal]) -> Dict[str, any]:
        flags = []
        
        # Rule 1: High Single Value Transfer
        if amount >= self.structuring_threshold:
            flags.append("CTR_TRIGGER_THRESHOLD_EXCEEDED")

        # Rule 2: Structuring Detection (Multiple transfers just under $10,000)
        recent_micro_txs = [tx for tx in recent_history if self.micro_tx_limit <= tx < self.structuring_threshold]
        if len(recent_micro_txs) >= 2:
            flags.append("POTENTIAL_STRUCTURING_SMURFING")

        return {
            "risk_score": 85 if flags else 10,
            "action": "FLAG_FOR_REVIEW" if flags else "APPROVE",
            "triggered_rules": flags
        }
