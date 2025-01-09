"""This modules contains the capitoltrades scraper for the trades page"""

from typing import List, Optional

from utils import make_request, parse_page_data, parse_trade_page, parse_trade_stats
from utils.dataclasses import Trade, TradesStats


class Trades:
    """Class responsible for scraping the capitoltrades trade page"""

    def __init__(self) -> None:
        """Constructor for the Trades class"""
        self._trades: Optional[List[Trade]] = None
        self._stats: Optional[TradesStats] = None
        self._total_pages: Optional[int] = None

    @property
    def trades(self) -> List[Trade]:
        """Return the total available trades"""
        if self._trades is not None:
            return self._trades

        # TODO: Scrape all site not just one page
        res = make_request("trades")
        self._trades = parse_trade_page(res.text)
        return self._trades

    @property
    def stats(self) -> TradesStats:
        """Return the total stats of trades"""
        if self._stats is not None:
            return self._stats

        res = make_request("trades")
        self._stats = parse_trade_stats(res.text)
        return self._stats

    @property
    def total_pages(self) -> int:
        """Return the total number of pages to scrape"""
        if self._total_pages is not None:
            return self._total_pages

        res = make_request("trades")
        self._total_pages = parse_page_data(res.text).total
        return self._total_pages
