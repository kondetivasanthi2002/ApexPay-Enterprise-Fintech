from fastapi import APIRouter
from apps.api.trading.market_data import MarketDataFeed

router = APIRouter(prefix="/api/v1/trading", tags=["Wealth & Trading Engine"])

@router.get("/ticker/{symbol}")
def get_ticker(symbol: str):
    return MarketDataFeed.generate_ticker_snapshot(symbol.upper(), 150.0)
