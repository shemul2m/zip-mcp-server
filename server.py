from mcp.server.fastmcp import FastMCP
import zipfile, io, base64, os

mcp = FastMCP("ZipServer")

@mcp.tool()
def create_zip(files: dict) -> str:
    """files = {"name.txt": "content"}"""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w') as z:
        for name, content in files.items():
            z.writestr(name, content)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    mcp.run(transport="sse", host="0.0.0.0", port=port)
