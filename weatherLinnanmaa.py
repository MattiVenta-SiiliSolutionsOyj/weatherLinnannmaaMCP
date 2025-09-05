from typing import Any
import httpx
from fastmcp import FastMCP

from typing import Any
from datetime import datetime
import json
import asyncio
import logging

# Initialize FastMCP server
mcp = FastMCP("weatherLinnanmaa")

# Constants
WEATHER_API_BASE = "https://weather.willab.fi/weather.json"
USER_AGENT = "linnanmaa_weather-app/1.0"


@mcp.tool()
async def get_current_weather_json() -> str:
    """Make a request to the LinnanMaa API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
          "Accept": "application/json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(WEATHER_API_BASE, headers=headers, timeout=30.0)
            response.raise_for_status()
            return json.dumps(response.json())  # Ensure return type is str
        except Exception as e:
            logging.error(f"Error fetching weather: {e}")
            return json.dumps({"error": "Failed to fetch weather data"})
       

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
