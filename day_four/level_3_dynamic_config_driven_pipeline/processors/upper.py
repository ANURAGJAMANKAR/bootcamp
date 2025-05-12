def to_uppercase(line: str) -> str:
    """
    Convert a string to uppercase.

    This function removes leading and trailing whitespace from the input string,
    then converts all characters to uppercase.

    Parameters:
        line (str): The input string to convert.

    Returns:
        str: The uppercase version of the input string.
    
    Example:
        >>> to_uppercase("  hello world  ")
        'HELLO WORLD'
    """
    # Remove leading/trailing spaces, then shout it out in uppercase
    return line.strip().upper()
