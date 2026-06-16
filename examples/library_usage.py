from datetime import datetime
from src.forex_pytory.core.scrapper import (
    forex_factory_scrapper,
    crypto_craft_scrapper,
    energy_exch_scrapper,
    metals_mine_scrapper,
)


def run_scraper(name, scrapper_module, dt):
    print(f"\n{'=' * 40}")
    print(f"Scraping {name}")
    print(f"{'=' * 40}")

    url = scrapper_module.get_url(day=dt.day, month=dt.month, year=dt.year, timeline="day")
    print(f"URL: {url}")

    try:
        records = scrapper_module.get_records(url)
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
        ("Forex Factory", forex_factory_scrapper),
        ("Crypto Craft", crypto_craft_scrapper),
        ("Energy Exch", energy_exch_scrapper),
        ("Metals Mine", metals_mine_scrapper),
    ]

    for name, module in scrapers_to_run:
        run_scraper(name, module, dt)


if __name__ == "__main__":
    main()
