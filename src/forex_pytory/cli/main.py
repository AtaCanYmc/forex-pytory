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
        from rich.console import Console
        from rich.table import Table
        from rich.panel import Panel

        console = Console()
        if not records:
            console.print(Panel("[yellow]No records found.[/yellow]", title="Economic Events"))
            return

        table = Table(title=f"Economic Events ({args.source.title()}) - {args.date or 'Today'}")
        table.add_column("ID", style="dim", no_wrap=True)
        table.add_column("Time", style="cyan", no_wrap=True)
        table.add_column("Currency", style="magenta", no_wrap=True)
        table.add_column("Event", style="green")
        table.add_column("Impact")
        table.add_column("Forecast")
        table.add_column("Actual", justify="right")
        table.add_column("Previous", justify="right")

        for r in records:
            impact_style = "default"
            if r.impact == "high":
                impact_style = "bold red"
            elif r.impact == "medium":
                impact_style = "bold yellow"
            elif r.impact == "low":
                impact_style = "yellow"

            table.add_row(
                r.id or "",
                r.time or "",
                r.currency or "",
                r.event or "",
                f"[{impact_style}]{r.impact or ''}[/]",
                r.forecast or "",
                r.actual or "",
                r.previous or ""
            )

        console.print(table)


if __name__ == "__main__":
    main()
