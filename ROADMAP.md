# Project Roadmap

This roadmap documents completed milestones and upcoming technical priorities for `forex-pytory`.

---

## Current Release: v0.2.1 <!-- x-release-please-version -->

- [x] Multi-source economic calendar extraction (ForexFactory, CryptoCraft, EnergyExch, MetalsMine).
- [x] Standardized Pydantic v2 data model (`EconomicEvent`).
- [x] Cloudflare challenge bypass via `cloudscraper`.
- [x] CLI utility with table and JSON output modes (`forex-scraper`).
- [x] Model Context Protocol (MCP) server implementation (`forex-mcp`).
- [x] MkDocs Material documentation hosted on GitHub Pages.
- [x] Release Please automated release management and CHANGELOG tracking.

---

## Upcoming Milestones

### v0.2.0 (Target: Q1 2027)

- [ ] **Custom Timezone Localization**: Add explicit `--timezone` flag and SDK parameter to normalize portal timestamps into local or UTC timezones.
- [ ] **Historical Date Range Scraping**: Enable date ranges (e.g. `--start-date` and `--end-date`) with automatic rate-limit throttling across consecutive dates.
- [ ] **Async SDK Support**: Provide native `asyncio` client interface for non-blocking calendar querying.

### v0.3.0 (Target: Q2 2027)

- [ ] **Filter Presets**: Add filtering capabilities for currency pairs (e.g. `USD`, `EUR`), impact levels (`high`, `medium`), and event keywords.
- [ ] **Event Impact Notification Webhook**: Lightweight webhook dispatcher to push scheduled high-impact events to external endpoints (Slack, Discord, Telegram).
