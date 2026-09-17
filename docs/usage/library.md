# Python SDK Usage

`forex-pytory` can be imported into Python projects, automated trading pipelines, and analytical notebooks.

---

## Basic Scraping Workflow

Every market has a dedicated scraper module under `forex_pytory.core.scraper`:

```python
from datetime import datetime
from forex_pytory.core.scraper import (
    forex_factory_scraper,
    crypto_craft_scraper,
    energy_exch_scraper,
    metals_mine_scraper,
)

# 1. Choose date
now = datetime.now()

# 2. Build target URL
url = forex_factory_scraper.get_url(day=now.day, month=now.month, year=now.year, timeline="day")

# 3. Fetch and parse records
events = forex_factory_scraper.get_records(url)

# 4. Iterate over typed EconomicEvent objects
for event in events:
    print(f"[{event.time}] {event.currency} - {event.event} (Impact: {event.impact})")
```

---

## EconomicEvent Data Model

Each event returned by `get_records()` is an instance of the `EconomicEvent` Pydantic model:

```python
from pydantic import BaseModel, Field
from typing import Optional

class EconomicEvent(BaseModel):
    id: Optional[str] = Field(default=None, alias="ID")
    time: Optional[str] = Field(default=None, alias="Time")
    currency: Optional[str] = Field(default=None, alias="Currency")
    event: Optional[str] = Field(default=None, alias="Event")
    forecast: Optional[str] = Field(default=None, alias="Forecast")
    actual: Optional[str] = Field(default=None, alias="Actual")
    previous: Optional[str] = Field(default=None, alias="Previous")
    impact: Optional[str] = Field(default=None, alias="Impact")
```

### Exporting to Pandas DataFrame

Because `EconomicEvent` is a standard Pydantic model, converting scraped results to a Pandas DataFrame requires a single line:

```python
import pandas as pd

df = pd.DataFrame([e.model_dump(by_alias=True) for e in events])
print(df.head())
```

---

## Error Handling

When scraping remote endpoints, handle network exceptions and parse errors cleanly:

```python
try:
    events = forex_factory_scraper.get_records(url)
except Exception as exc:
    print(f"Failed to scrape calendar: {exc}")
```
