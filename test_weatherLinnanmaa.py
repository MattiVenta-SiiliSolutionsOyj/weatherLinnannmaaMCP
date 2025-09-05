import asyncio
import httpx
import json

# Constants (copied from weatherLinnanmaa.py)
WEATHER_API_BASE = "https://weather.willab.fi/weather.json"
USER_AGENT = "linnanmaa_weather-app/1.0"

async def test_get_current_weather_json_success():
    """Test the weather function by calling the underlying function directly"""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(WEATHER_API_BASE, headers=headers, timeout=30.0)
            response.raise_for_status()
            return json.dumps(response.json())
        except Exception as e:
            print(f"Error fetching weather: {e}")
            return json.dumps({"error": "Failed to fetch weather data"})

print("Running test for get_current_weather_json...")
result = asyncio.run(test_get_current_weather_json_success())
print("Test Result:")
print(result)
