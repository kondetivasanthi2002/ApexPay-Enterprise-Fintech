from decimal import Decimal
from typing import List, Dict

class TaxLot:
    def __init__(self, lot_id: str, symbol: str, quantity: Decimal, purchase_price: Decimal):
        self.lot_id = lot_id
        self.symbol = symbol
        self.quantity = quantity
        self.purchase_price = purchase_price

class PortfolioValuationEngine:
    def __init__(self):
        self.tax_lots: Dict[str, List[TaxLot]] = {}

    def add_position(self, symbol: str, lot_id: str, quantity: Decimal, price: Decimal):
        if symbol not in self.tax_lots:
            self.tax_lots[symbol] = []
        self.tax_lots[symbol].append(TaxLot(lot_id, symbol, quantity, price))

    def sell_position_fifo(self, symbol: str, quantity_to_sell: Decimal, current_price: Decimal) -> Dict[str, any]:
        if symbol not in self.tax_lots or not self.tax_lots[symbol]:
            raise ValueError(f"No position available in {symbol}")

        realized_gain = Decimal("0.00")
        remaining_to_sell = quantity_to_sell

        while remaining_to_sell > 0 and self.tax_lots[symbol]:
            lot = self.tax_lots[symbol][0]
            sell_qty = min(remaining_to_sell, lot.quantity)

            gain = sell_qty * (current_price - lot.purchase_price)
            realized_gain += gain

            lot.quantity -= sell_qty
            remaining_to_sell -= sell_qty

            if lot.quantity == 0:
                self.tax_lots[symbol].pop(0)

        return {
            "symbol": symbol,
            "realized_gain_loss": str(realized_gain),
            "units_sold": str(quantity_to_sell - remaining_to_sell)
        }
