"""This modules contains the capitoltrades scraper for the trades page"""

from .meta import TradesMeta


class Trades:
    """Class responsible for scraping the capitoltrades trade page"""

    def __init__(self) -> None:
        """Constructor for the Trades class"""
        pass

    def stats(self) -> TradesMeta:
        """Return the total stats of trades"""
        if hasattr(self, "meta"):
            return self._meta
        else:
            # TODO: set this value from scraping
            self._meta = TradesMeta(1, 1, "1", 1, 1)
            return self._meta
