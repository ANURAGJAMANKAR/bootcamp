from processor_types import ProcessorFn
from typing import Iterator

def apply_pipeline(lines: Iterator[str], processors: list[ProcessorFn]) -> Iterator[str]:
    """
    Apply a sequence of processor functions to each line in the input.

    This function takes an iterator of strings (lines) and a list of processor
    functions. Each line is passed through the processors in order, and the
    final result is yielded one by one as an iterator.

    Parameters:
        lines (Iterator[str]): An iterator of input lines (e.g., from a file).
        processors (list[ProcessorFn]): A list of functions, each taking a string
                                        and returning a transformed string.

    Returns:
        Iterator[str]: An iterator of processed lines.

    Example:
        If processors = [strip, to_uppercase], then each line will first be
        stripped of whitespace and then converted to uppercase.

        >>> list(apply_pipeline(iter(["  hello ", " world"]), [str.strip, str.upper]))
        ['HELLO', 'WORLD']
    """
    # Process each line through the pipeline
    for line in lines:
        for processor in processors:
            # Apply each processor function to the line in sequence
            line = processor(line)
        yield line  # Return the final transformed line
