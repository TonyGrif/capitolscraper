"""This modules contains the capitoltrades scraper for the trades page"""

from utils import make_request, parse_trade_stats

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
            res = make_request()

            # TODO: raise this in function with httpx exceptions
            if res.status_code != 200:
                raise ValueError

            data = parse_trade_stats(res.text)

            self._meta = TradesMeta(
                int(data[0].replace(",", "")),
                int(data[1].replace(",", "")),
                data[2],
                int(data[3].replace(",", "")),
                int(data[4].replace(",", "")),
            )
            return self._meta
