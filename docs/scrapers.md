# Supported Markets & Scrapers

`forex-pytory` unifies access across four major financial portals operated under the ForexFactory umbrella.

---

## Market Endpoints

| Market | Source Domain | Scraper Module | Default Currency Filter |
| :--- | :--- | :--- | :--- |
| **Forex** | `forexfactory.com` | `forex_pytory.core.scraper.forex_factory_scraper` | Global fiat pairs (USD, EUR, GBP, JPY, CAD, AUD, NZD, CHF) |
| **Crypto** | `cryptocraft.com` | `forex_pytory.core.scraper.crypto_craft_scraper` | Major cryptocurrency assets (BTC, ETH, SOL, etc.) |
| **Energy** | `energyexch.com` | `forex_pytory.core.scraper.energy_exch_scraper` | Oil, natural gas, gasoline, and power releases |
| **Metals** | `metalsmine.com` | `forex_pytory.core.scraper.metals_mine_scraper` | Gold, silver, copper, platinum releases |

---

## URL Generation Mechanics

Each scraper module contains a `get_url()` function that constructs valid portal URLs based on calendar parameters:

```python
def get_url(day: int, month: int, year: int, timeline: str = "day") -> str
```

Supported timeline arguments:
- `day`: Single calendar day.
- `week`: Full calendar week containing the specified date.
- `month`: Full calendar month containing the specified date.

---

## Anti-Bot & Network Caveats

- **Cloudflare Session**: Scrapers instantiate a `cloudscraper` session with browser user-agent spoofing to satisfy Cloudflare challenge responses.
- **Rate Limits**: Excessive parallel requests against these domains may result in HTTP 429 or temporary IP throttling. Space recurring polling intervals appropriately.
- **Timezone Offsets**: Portal timestamps correspond to session cookie settings. By default, unauthenticated scrapes return Eastern Time (EST/EDT).
