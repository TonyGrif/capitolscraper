import pytest

from scraper import Trades


@pytest.fixture(scope="function")
def trades():
    return Trades()


class TestTrades:
    def test_trades(self, trades):
        trade_collection = trades.trades

        assert len(trade_collection) == 12
        assert trade_collection[0].politician is not None

        assert trade_collection == trades.trades

    def test_stats(self, trades):
        first_stats = trades.stats
        assert first_stats.trades is not None
        assert first_stats.filings is not None
        assert first_stats.volume is not None
        assert first_stats.politicians is not None
        assert first_stats.issuers is not None

        second_stats = trades.stats
        assert second_stats.trades == first_stats.trades
        assert second_stats.filings == first_stats.filings
        assert second_stats.volume == first_stats.volume
        assert second_stats.politicians == first_stats.politicians
        assert second_stats.issuers == first_stats.issuers

    def test_total_pages(self, trades):
        first = trades.total_pages
        assert first is not None

        second = trades.total_pages
        assert second == first
