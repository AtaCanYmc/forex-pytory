import json
import logging
from datetime import datetime
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio
import mcp.types as types

from src.forex_pytory.core.scrapper import (
    forex_factory_scrapper,
    crypto_craft_scrapper,
    energy_exch_scrapper,
    metals_mine_scrapper,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("forex-pytory-mcp")

server = Server("forex-pytory")


@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="fetch_economic_events",
            description="Fetch economic calendar events from ForexFactory, CryptoCraft, EnergyExch, or MetalsMine.",
            inputSchema={
                "type": "object",
                "properties": {
                    "source": {
                        "type": "string",
                        "description": "Source to scrape",
                        "enum": ["forex", "crypto", "energy", "metals"]
                    },
                    "date": {
                        "type": "string",
                        "description": "Date to scrape in YYYY-MM-DD format. If omitted, uses today's date."
                    }
                },
                "required": ["source"]
            }
        )
    ]


@server.call_tool()
async def handle_call_tool(
        name: str, arguments: dict | None
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    if name != "fetch_economic_events":
        raise ValueError(f"Unknown tool: {name}")

    if not arguments:
        raise ValueError("Missing arguments")

    source = arguments.get("source")
    date_str = arguments.get("date")

    if source not in ["forex", "crypto", "energy", "metals"]:
        raise ValueError(f"Invalid source: {source}")

    if date_str:
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            day, month, year = dt.day, dt.month, dt.year
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    else:
        dt = datetime.now()
        day, month, year = dt.day, dt.month, dt.year

    scrappers = {
        "forex": forex_factory_scrapper,
        "crypto": crypto_craft_scrapper,
        "energy": energy_exch_scrapper,
        "metals": metals_mine_scrapper,
    }

    scrapper = scrappers[source]
    url = scrapper.get_url(day=day, month=month, year=year, timeline="day")

    try:
        records = scrapper.get_records(url)
    except Exception as e:
        logger.error(f"Scraping failed: {e}")
        return [types.TextContent(type="text", text=f"Error scraping data: {e}")]

    result_json = json.dumps([r.model_dump(by_alias=True) for r in records], indent=2)
    return [
        types.TextContent(
            type="text",
            text=result_json
        )
    ]


async def run_server():
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="forex-pytory",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


if __name__ == "__main__":
    import asyncio

    asyncio.run(run_server())
