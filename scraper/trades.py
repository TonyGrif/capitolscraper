"""This modules contains the capitoltrades scraper for the trades page"""

from typing import Optional

from utils import make_request, parse_trade_stats
from utils.dataclasses import TradesStats


class Trades:
    """Class responsible for scraping the capitoltrades trade page"""

    def __init__(self) -> None:
        """Constructor for the Trades class"""
        self._stats: Optional[TradesStats] = None

    def stats(self) -> TradesStats:
        """Return the total stats of trades"""
        if self._stats is not None:
            return self._stats

        res = make_request("trades")
        self._stats = parse_trade_stats(res.text)
        return self._stats
