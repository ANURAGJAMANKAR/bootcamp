from typing import Callable

"""
Type alias for processor functions used in the text transformation pipeline.

A ProcessorFn is any function that:
- Takes a single string argument (the line to transform)
- Returns a string (the transformed result)

Example:
    def to_upper(line: str) -> str:
        return line.upper()
"""

ProcessorFn = Callable[[str], str]
