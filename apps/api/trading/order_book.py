from enum import Enum
from decimal import Decimal
from typing import List, Dict
from pydantic import BaseModel

class OrderType(str, Enum):
    LIMIT = "LIMIT"
    MARKET = "MARKET"

class OrderSide(str, Enum):
    BUY = "BUY"
    SELL = "SELL"

class Order(BaseModel):
    order_id: str
    symbol: str
    side: OrderSide
    order_type: OrderType
    price: Decimal
    quantity: Decimal
    filled_qty: Decimal = Decimal("0.00")

class LimitOrderBook:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.bids: List[Order] = [] # Buy orders sorted high to low
        self.asks: List[Order] = [] # Sell orders sorted low to high

    def add_order(self, order: Order) -> List[Dict[str, any]]:
        trades = []
        if order.side == OrderSide.BUY:
            self.bids.append(order)
            self.bids.sort(key=lambda x: x.price, reverse=True)
        else:
            self.asks.append(order)
            self.asks.sort(key=lambda x: x.price)

        trades = self.match_orders()
        return trades

    def match_orders(self) -> List[Dict[str, any]]:
        trades = []
        while self.bids and self.asks and self.bids[0].price >= self.asks[0].price:
            best_bid = self.bids[0]
            best_ask = self.asks[0]

            exec_qty = min(best_bid.quantity - best_bid.filled_qty, best_ask.quantity - best_ask.filled_qty)
            exec_price = best_ask.price

            best_bid.filled_qty += exec_qty
            best_ask.filled_qty += exec_qty

            trades.append({
                "symbol": self.symbol,
                "price": str(exec_price),
                "quantity": str(exec_qty),
                "buyer_order_id": best_bid.order_id,
                "seller_order_id": best_ask.order_id
            })

            if best_bid.filled_qty >= best_bid.quantity:
                self.bids.pop(0)
            if best_ask.filled_qty >= best_ask.quantity:
                self.asks.pop(0)

        return trades
