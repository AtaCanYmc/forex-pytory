from datetime import datetime
from src.forex_pytory.core.scraper import (
    forex_factory_scraper,
    crypto_craft_scraper,
    energy_exch_scraper,
    metals_mine_scraper,
)


def run_scraper(name, scraper_module, dt):
    print(f"\n{'=' * 40}")
    print(f"Scraping {name}")
    print(f"{'=' * 40}")

    url = scraper_module.get_url(day=dt.day, month=dt.month, year=dt.year, timeline="day")
    print(f"URL: {url}")

    try:
        records = scraper_module.get_records(url)
        print(f"Found {len(records)} events:")

        # Sadece ilk 3 tanesini yazdıralım ki çok uzun olmasın
        for r in records[:3]:
            # r is a Pydantic model (EconomicEvent)
            print(f"[{r.time}] {r.currency} - {r.event[:30]}... (Impact: {r.impact})")

        if len(records) > 3:
            print(f"... and {len(records) - 3} more.")

    except Exception as e:
        print(f"Error fetching records: {e}")


def main():
    dt = datetime.now()

    scrapers_to_run = [
        ("Forex Factory", forex_factory_scraper),
        ("Crypto Craft", crypto_craft_scraper),
        ("Energy Exch", energy_exch_scraper),
        ("Metals Mine", metals_mine_scraper),
    ]

    for name, module in scrapers_to_run:
        run_scraper(name, module, dt)


if __name__ == "__main__":
    main()
