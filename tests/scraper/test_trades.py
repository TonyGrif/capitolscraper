from scraper.trades import Trades
import pytest


@pytest.fixture
def trades():
    return Trades()


class TestTrades:
    def test_meta_stats(self, trades):
        meta = trades.stats()

        assert meta.trades == 1
        assert meta.filings == 1
        assert meta.volume == "1"
        assert meta.politicians == 1
        assert meta.issuers == 1
