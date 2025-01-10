"""This module contains utility dataclasses for the capitolscraper"""

from .page_data import PageData
from .trade import Politician, Trade
from .trade_stats import TradesStats
from .traded_issuer import IssuedTrader

__all__ = ["IssuedTrader", "PageData", "TradesStats", "Politician", "Trade"]
