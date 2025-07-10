from mcp.server.fastmcp import FastMCP
import tools

mcp = FastMCP("host info mcp")
mcp.add_tool(tools.get_host_info)

def main():
    mcp.run("stdio")

if __name__ == "__main__":
    main()