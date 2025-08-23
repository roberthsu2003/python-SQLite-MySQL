## Postgres MCP Server
- [官網連結](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/postgres)

**postgres SQL in docker**

```mcp
{
  "servers": {
    "vscode_postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "postgresql://postgres:raspberry@host.docker.internal:5432/postgres"
      ]
    }
  },
}

```