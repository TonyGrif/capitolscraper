"""This modules contains the capitoltrades scraper for the trades page"""

from typing import Optional

from utils import make_request, parse_trade_stats

from .stats import TradesStats


class Trades:
    """Class responsible for scraping the capitoltrades trade page"""

    def __init__(self) -> None:
        """Constructor for the Trades class"""
        self._stats: Optional[TradesStats] = None

    def stats(self) -> TradesStats:
        """Return the total stats of trades"""
        if self._stats is not None:
            return self._stats

        res = make_request()

        # TODO: raise this in function with httpx exceptions
        if res.status_code != 200:
            raise ValueError

        data = parse_trade_stats(res.text)

        self._stats = TradesStats(
            int(data[0].replace(",", "")),
            int(data[1].replace(",", "")),
            data[2],
            int(data[3].replace(",", "")),
            int(data[4].replace(",", "")),
        )
        return self._stats
