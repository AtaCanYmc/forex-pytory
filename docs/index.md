# Forex-Pytory

A Python library, CLI, and Model Context Protocol (MCP) server for extracting structured economic calendar events across Forex, Cryptocurrency, Energy, and Precious Metals markets.

---

## Highlights

- **Multi-Market Coverage**: Scrapes calendar events from ForexFactory, CryptoCraft, EnergyExch, and MetalsMine.
- **Strict Pydantic Validation**: Converts raw HTML tables into strongly-typed `EconomicEvent` data structures.
- **Built-in Cloudflare Bypass**: Employs `cloudscraper` to resolve anti-bot JavaScript hurdles.
- **Three Consumption Interfaces**: Use directly as a Python module, run via terminal CLI, or link into AI agents via MCP.

---

## Architecture Overview

```mermaid
flowchart TD
    Sources["Financial Portals<br>(ForexFactory / CryptoCraft / EnergyExch / MetalsMine)"]
    HTTP["HTTP Transport<br>(cloudscraper session)"]
    Parser["DOM Parser<br>(BeautifulSoup4)"]
    Validation["Validation Engine<br>(Pydantic v2 EconomicEvent)"]

    subgraph Consumers["Interfaces"]
        CLI["CLI Tool<br>(forex-scraper)"]
        SDK["Python SDK<br>(forex_pytory)"]
        MCP["MCP Server<br>(forex-mcp stdio)"]
    end

    Sources -->|"HTML over HTTPS"| HTTP
    HTTP -->|"DOM Elements"| Parser
    Parser -->|"Extracted Dicts"| Validation
    Validation -->|"Formatted Output"| CLI
    Validation -->|"list[EconomicEvent]"| SDK
    Validation -->|"JSON-RPC Tool Response"| MCP
```

---

## Quick Navigation

- [Getting Started](getting-started.md): Installation and environment preparation.
- [Python SDK Guide](usage/library.md): Using `forex-pytory` in Python code and scripts.
- [CLI Reference](usage/cli.md): Running `forex-scraper` from your terminal.
- [MCP Server Setup](usage/mcp.md): Connecting the scraper to Claude Desktop and Cursor.
- [Supported Markets](scrapers.md): Details on supported financial portals and URL formats.
- [Contributing](contributing.md): Developer workflow and Makefile targets.
