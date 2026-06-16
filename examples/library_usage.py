from datetime import datetime
from src.forex_pytory.core.scrapper import forex_factory_scrapper


def main():
    dt = datetime.now()
    url = forex_factory_scrapper.get_url(day=dt.day, month=dt.month, year=dt.year, timeline="day")

    print(f"Scraping from: {url}")
    records = forex_factory_scrapper.get_records(url)

    print(f"Found {len(records)} events:")
    for r in records:
        # r is a Pydantic model (EconomicEvent)
        print(f"[{r.time}] {r.currency} - {r.event} (Impact: {r.impact})")


if __name__ == "__main__":
    main()
