from typing import Iterator

from process_types import ProcessorFn, ProcessorList

def process_line(line: str, processors: ProcessorList) -> str:
    """Apply a list of processors to a line in sequence."""
    result = line
    for processor in processors:
        result = processor(result)
    return result

def process_lines(lines: Iterator[str], processors: ProcessorList) -> Iterator[str]:
    """Process each line using the provided processors."""
    for line in lines:
        yield process_line(line, processors)
