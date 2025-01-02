from utils import make_request, parse_trade_stats
import pytest


@pytest.fixture
def res():
    return make_request()


def test_make_request(res):
    assert res.status_code == 200
    assert res.text is not None


def test_parse_trade_stats(res):
    data = parse_trade_stats(res)
    assert len(data) == 5
