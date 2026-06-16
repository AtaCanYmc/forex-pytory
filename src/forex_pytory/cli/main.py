import argparse
import json
import sys
from datetime import datetime
from ..core.scrapper import (
    forex_factory_scrapper,
    crypto_craft_scrapper,
    energy_exch_scrapper,
    metals_mine_scrapper,
)


def main():
    parser = argparse.ArgumentParser(description="Scrape economic events.")
    parser.add_argument("--source", type=str, choices=["forex", "crypto", "energy", "metals"], default="forex",
                        help="Source to scrape")
    parser.add_argument("--date", type=str, help="Date to scrape in YYYY-MM-DD format (default: today)")
    parser.add_argument("--format", type=str, choices=["json", "table"], default="json", help="Output format")

    args = parser.parse_args()

    if args.date:
        try:
            dt = datetime.strptime(args.date, "%Y-%m-%d")
            day, month, year = dt.day, dt.month, dt.year
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD.")
            sys.exit(1)
    else:
        dt = datetime.now()
        day, month, year = dt.day, dt.month, dt.year

    scrappers = {
        "forex": forex_factory_scrapper,
        "crypto": crypto_craft_scrapper,
        "energy": energy_exch_scrapper,
        "metals": metals_mine_scrapper,
    }

    scrapper = scrappers[args.source]
    url = scrapper.get_url(day=day, month=month, year=year, timeline="day")

    try:
        records = scrapper.get_records(url)
    except Exception as e:
        print(f"Error scraping data: {e}", file=sys.stderr)
        sys.exit(1)

    if args.format == "json":
        print(json.dumps([r.model_dump(by_alias=True) for r in records], indent=2))
    else:
        # Simple table format
        if not records:
            print("No records found.")
            return

        headers = ["ID", "Time", "Currency", "Event", "Impact", "Forecast", "Actual", "Previous"]
        row_format = "{:<15} | {:<10} | {:<8} | {:<40} | {:<8} | {:<10} | {:<10} | {:<10}"
        print(row_format.format(*headers))
        print("-" * 120)
        for r in records:
            print(row_format.format(
                r.id or "", r.time or "", r.currency or "", (r.event or "")[:38],
                r.impact or "", r.forecast or "", r.actual or "", r.previous or ""
            ))


if __name__ == "__main__":
    main()
