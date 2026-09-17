# Model Context Protocol (MCP) Server

`forex-pytory` implements an official Model Context Protocol (MCP) server that enables AI assistants (such as Claude Desktop, Cursor, or custom LLM agents) to query economic calendar releases as callable tools.

---

## Architecture

The MCP server runs locally and communicates with host applications over standard input and output (`stdio`):

```mermaid
sequenceDiagram
    autonumber
    actor User as User / Prompt
    participant Agent as LLM Agent (Claude)
    participant Server as forex-mcp Server
    participant Scraper as Scraper Engine

    User->>Agent: "What high-impact Forex releases are scheduled today?"
    Agent->>Server: tools/call fetch_economic_events {"source": "forex"}
    Server->>Scraper: Fetch calendar & parse DOM
    Scraper-->>Server: list[EconomicEvent]
    Server-->>Agent: JSON-RPC Result (Event Payload)
    Agent-->>User: Summarized release report
```

---

## Claude Desktop Configuration

Locate your Claude Desktop configuration file:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

Add the server configuration under the `mcpServers` block:

```json
{
  "mcpServers": {
    "forex-pytory": {
      "command": "/absolute/path/to/forex-pytory/.venv/bin/forex-mcp",
      "args": []
    }
  }
}
```

Restart Claude Desktop. The hammer icon in the interface will display the `fetch_economic_events` tool.

---

## Tool Specification

### `fetch_economic_events`

Fetches economic calendar events from the specified market source.

**Parameters**:

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `source` | String | Yes | Market source: `forex`, `crypto`, `energy`, or `metals`. |
| `date` | String | No | Date in `YYYY-MM-DD` format. Defaults to today's date if omitted. |
