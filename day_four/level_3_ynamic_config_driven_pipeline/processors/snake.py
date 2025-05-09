def to_snakecase(line: str) -> str:
    """Convert a line to snakecase (replace spaces with underscores and lowercase)."""
    return line.replace(" ", "_").lower()
