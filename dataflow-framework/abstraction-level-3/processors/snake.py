def to_snakecase(line: str) -> str:
    """
    Convert a string to snake_case.

    This function takes a string, strips leading and trailing whitespace,
    replaces all spaces with underscores, and converts the entire string to lowercase.

    Parameters:
        line (str): The input string to convert.

    Returns:
        str: The snake_case version of the input string.
    
    Example:
        >>> to_snakecase("Hello World")
        'hello_world'
    """
    # Strip leading/trailing spaces, replace inner spaces with underscores, and lowercase it all
    return line.strip().replace(" ", "_").lower()
