# tools/file_reader.py

from langchain.tools import tool

@tool
def file_reader_tool(path: str) -> str:
    """Read and return the contents of a local file given its path."""
    try:
        with open(path, 'r') as file:
            return file.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"
