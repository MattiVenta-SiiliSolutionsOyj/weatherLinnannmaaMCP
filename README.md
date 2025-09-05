## MCP-serverin testaaminen

1. Varmista, että MCP-serveri on käynnissä:
   ```bash
   uv run weatherLinnanmaa.py
   ```

2. Testaa MCP-clientilla (esim. Python-skripti):

   ```python
   from fastmcp.client import Client
   import asyncio

   async def main():
       client = Client("weatherLinnanmaa", transport="stdio")
       result = await client.call_tool("get_current_weather_json")
       print(result)

   asyncio.run(main())
   ```

3. Suorita testiskripti:
   ```bash
   python test_mcp_client.py
   ```

Jos saat JSON-muotoisen säädatan, MCP-serveri toimii oikein!