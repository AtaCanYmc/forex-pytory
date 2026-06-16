import asyncio
from src.forex_pytory.mcp.server import run_server

if __name__ == "__main__":
    print("Starting MCP Server...")
    print("This server expects to communicate over stdio.")
    asyncio.run(run_server())
