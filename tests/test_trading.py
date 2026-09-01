import pytest
from decimal import Decimal
from apps.api.trading.order_book import LimitOrderBook, Order, OrderSide, OrderType
from apps.api.trading.portfolio import PortfolioValuationEngine

def test_order_book_limit_matching():
    book = LimitOrderBook("AAPL")
    buy_order = Order(order_id="O1", symbol="AAPL", side=OrderSide.BUY, order_type=OrderType.LIMIT, price=Decimal("150.00"), quantity=Decimal("10"))
    sell_order = Order(order_id="O2", symbol="AAPL", side=OrderSide.SELL, order_type=OrderType.LIMIT, price=Decimal("149.00"), quantity=Decimal("10"))

    book.add_order(buy_order)
    trades = book.add_order(sell_order)

    assert len(trades) == 1
    assert trades[0]["price"] == "149.00"

def test_portfolio_tax_lot_fifo():
    engine = PortfolioValuationEngine()
    engine.add_position("AAPL", "LOT-1", Decimal("10"), Decimal("100.00"))
    res = engine.sell_position_fifo("AAPL", Decimal("5"), Decimal("150.00"))
    assert res["realized_gain_loss"] == "250.00"
