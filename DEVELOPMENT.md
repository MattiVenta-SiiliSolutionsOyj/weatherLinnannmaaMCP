# Weather LinnanMaa MCP - Development Guide

## Project Overview
This MCP (Model Context Protocol) server provides real-time weather data for Linnanmaa area using the Willab.fi weather API.

## Quick Start

### 1. Environment Setup
```bash
# Install UV package manager
curl -LsSf https://astral.sh/uv/install.sh | sh

# Set up project environment
cd weatherLinnannmaa
uv venv
source .venv/bin/activate  # On macOS/Linux
uv sync
```

### 2. Testing
```bash
# Test MCP server
source .venv/bin/activate
uv run weatherLinnanmaa.py

# Test MCP client
python3 test_mcp_client.py

# Test weather API directly
python3 test_weatherLinnanmaa.py
```

### 3. Claude Desktop Integration
Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "weatherLinnanmaa": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/weatherLinnannmaa",
        "run",
        "weatherLinnanmaa.py"
      ]
    }
  }
}
```

## Development Rules

### MCP Server Structure
- Use `@mcp.tool()` decorator for exposed functions
- Initialize with `FastMCP("server_name")`
- Run with `mcp.run(transport='stdio')`
- Keep server initialization in main block

### API Integration
- Use `httpx.AsyncClient` with timeout ≥30s
- Include User-Agent headers
- Handle HTTP errors with `raise_for_status()`
- Always return JSON strings for consistency
- Implement comprehensive error handling with logging

### Weather API Specifics
- Base URL: `https://weather.willab.fi/weather.json`
- Returns: tempnow, templo, temphi, airpressure, humidity, precipitation, wind data
- User-Agent: "linnanmaa_weather-app/1.0"

### Code Style
- Always use type hints for function parameters and return values
- Use async functions for MCP tools
- Define constants in UPPER_CASE at module level
- Clear docstrings for all MCP tool functions

## File Organization
```
weatherLinnannmaa/
├── weatherLinnanmaa.py      # Main MCP server
├── test_mcp_client.py       # MCP client tests
├── test_weatherLinnanmaa.py # Direct API tests
├── main.py                  # Alternative entry point
├── pyproject.toml           # Dependencies
├── README.md                # User documentation
├── DEVELOPMENT.md           # This file
└── vscode-mcp-config/       # VS Code integration
```

## Troubleshooting

### MCP Server Issues
1. Check virtual environment: `source .venv/bin/activate`
2. Update dependencies: `uv sync`
3. Test syntax: `python3 -m py_compile weatherLinnanmaa.py`

### API Issues
1. Test API: `curl https://weather.willab.fi/weather.json`
2. Check internet connection
3. Verify User-Agent header

### Claude Integration
1. Use absolute paths in config
2. Restart Claude Desktop after changes
3. Test MCP server independently first

## Finnish Localization
- Support both Finnish and English responses
- Use Celsius for temperature (Finnish standard)
- Finnish terms: sää, lämpötila, tuuli, sade, kosteus, ilmanpaine
- Use metric units throughout

## Development Workflow
1. Activate environment: `source .venv/bin/activate`
2. Add dependencies: `uv add package_name`
3. Format code: `uv run ruff format .`
4. Test changes: Run all test files
5. Update Claude config if needed
6. Commit with descriptive messages