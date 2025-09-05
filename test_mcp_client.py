import asyncio
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters

async def test_mcp_client():
    """Test the MCP client connection to weatherLinnanmaa server"""
    
    # Create server parameters for the weather server
    server_params = StdioServerParameters(
        command="python",
        args=["weatherLinnanmaa.py"]
    )
    
    # Create stdio client transport
    async with stdio_client(server_params) as (read, write):
        # Create client session
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()
            
            # List available tools
            tools = await session.list_tools()
            print("Available tools:", [tool.name for tool in tools.tools])
            
            # Call the weather tool
            result = await session.call_tool("get_current_weather_json", {})
            print("Weather data:", result.content)

if __name__ == "__main__":
    print("Testing MCP client connection...")
    asyncio.run(test_mcp_client())
