import pytest

from scraper import Trades


@pytest.fixture
def trades():
    return Trades()


class TestTrades:
    def test_meta_stats(self, trades):
        meta = trades.stats()

        assert meta.trades is not None
        assert meta.filings is not None
        assert meta.volume is not None
        assert meta.politicians is not None
        assert meta.issuers is not None
