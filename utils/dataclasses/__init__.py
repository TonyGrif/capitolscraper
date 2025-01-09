"""This module contains utility dataclasses for the capitolscraper"""

from .page_data import PageData
from .trade import Politician, Trade
from .trade_stats import TradesStats

__all__ = ["PageData", "TradesStats", "Politician", "Trade"]
