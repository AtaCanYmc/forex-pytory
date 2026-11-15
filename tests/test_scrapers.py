from datetime import datetime
from forex_pytory.core.scraper import (
    forex_factory_scraper,
    crypto_craft_scraper,
    energy_exch_scraper,
    metals_mine_scraper,
)
from forex_pytory.core.scraper.common import to_24h


def test_url_generation():
    ff_url = forex_factory_scraper.get_url(day=15, month=9, year=2026, timeline="day")
    assert "forexfactory.com/calendar?day=Sep15.2026" in ff_url

    crypto_url = crypto_craft_scraper.get_url(day=1, month=1, year=2026, timeline="day")
    assert "cryptocraft.com/calendar?day=Jan1.2026" in crypto_url

    energy_url = energy_exch_scraper.get_url(day=20, month=5, year=2026, timeline="day")
    assert "energyexch.com/calendar?day=May20.2026" in energy_url

    metals_url = metals_mine_scraper.get_url(
        day=31, month=12, year=2026, timeline="day"
    )
    assert "metalsmine.com/calendar?day=Dec31.2026" in metals_url


def test_time_conversion():
    dt_am = to_24h(15, 9, 2026, "8:30am")
    assert dt_am.hour == 8
    assert dt_am.minute == 30

    dt_pm = to_24h(15, 9, 2026, "1:15pm")
    assert dt_pm.hour == 13
    assert dt_pm.minute == 15

    dt_all_day = to_24h(15, 9, 2026, "All Day")
    assert dt_all_day == datetime(2026, 9, 15, 0, 0)
