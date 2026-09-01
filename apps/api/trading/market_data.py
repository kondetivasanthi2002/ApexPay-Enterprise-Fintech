import random
from decimal import Decimal
from typing import Dict

class MarketDataFeed:
    @staticmethod
    def generate_ticker_snapshot(symbol: str, base_price: float) -> Dict[str, str]:
        change_pct = random.uniform(-0.02, 0.02)
        price = round(base_price * (1 + change_pct), 2)
        return {
            "symbol": symbol,
            "last_price": str(price),
            "high": str(round(price * 1.015, 2)),
            "low": str(round(price * 0.985, 2)),
            "volume_24h": str(random.randint(10000, 500000))
        }
