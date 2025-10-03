import os
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()

SMITHERY_API_KEY = os.getenv("SMITHERY_API_KEY")

MCP_SERVERS_CONFIG = {
    "yfinance": {
        "url": f"https://server.smithery.ai/@hwangwoohyun-nav/yahoo-finance-mcp/mcp?api_key={SMITHERY_API_KEY}",
        "transport": "streamable_http",
        "timeout": timedelta(seconds=60),
    }
    # "yfinance": {
    #     "url": "http://localhost:8001/mcp",
    #     "transport": "streamable_http",
    #     "timeout": timedelta(seconds=60),
    # }
}
