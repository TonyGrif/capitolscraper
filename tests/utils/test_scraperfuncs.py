from pathlib import Path

import httpx
import pytest

from utils import make_request, parse_page_data, parse_trade_page, parse_trade_stats


@pytest.fixture
def tradepage():
    return Path("tests/resources/01-02-2025_tradepage.txt")


def test_make_request():
    res = make_request("trades")
    assert res.status_code == 200
    assert res.text is not None

    with pytest.raises(httpx.HTTPStatusError):
        res = make_request("notreal")


def test_parse_trade_page(tradepage):
    with open(tradepage, "r") as f:
        data = parse_trade_page(str(f.readlines()))

        assert len(data) == 12

        pol = data[0].politician
        assert pol.name == "Tom Carper"
        assert pol.party == "Democrat"
        assert pol.chamber == "Senate"
        assert pol.state == "DE"

        issuer = data[0].issuer
        assert issuer.name == "Atlantica Sustainable Infrastructure PLC"
        assert issuer.symbol == "AY:US"

        dates = data[0].dates
        assert dates.published is not None
        assert dates.traded is not None
        assert dates.filed_after == 20

        assert data[0].owner == "Spouse"
        assert data[0].action == "Sell"


def test_parse_page_data(tradepage):
    with open(tradepage, "r") as f:
        data = parse_page_data(str(f.readlines()))

        assert data.current == 1
        assert data.total == 2983


def test_parse_trade_stats(tradepage):
    with open(tradepage, "r") as f:
        data = parse_trade_stats(str(f.readlines()))

        assert data.trades == 35791
        assert data.filings == 1743
        assert data.volume == "$2.161B"
        assert data.politicians == 204
        assert data.issuers == 3147
