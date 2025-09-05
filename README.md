## Set up your environment

1. Install `uv` and set up your Python project environment:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```



2. Create and set up your Python project:

   ```bash
   # Create a new directory for our project
   uv init weather
   cd weather

   # Create virtual environment and activate it
   uv venv
   source .venv/bin/activate

   # Install dependencies
   uv add "mcp[cli]" httpx

   # Create our server file
   touch weather.py
   ```


## Testing with claude desctop

Add mcpServers config to 

~/Library/Application\ Support/Claude/claude_desktop_config.json
```
{
  "mcpServers": {
    "weather": {
      "command": " /ABSOLUTE/PATH/TO/ uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/weatherLinnanmaa",
        "run",
        "weather.py"
      ]
    }
  }
}
```
Save the file, and restart Claude for Desktop.

## VS-CodeAndgithubCo pilot



## Testing from terminal MCP-server

1. Activate virtual enviroment it source .venv/bin/activate
   ```bash
   source .venv/bin/activate
   ```
2. Käynnistä MCP-serveri:
   ```bash
   uv run weatherLinnanmaa.py
   ```

3. Testaa MCP-clientia:
   ```bash
   python3 test_mcp_client.py
   ```




