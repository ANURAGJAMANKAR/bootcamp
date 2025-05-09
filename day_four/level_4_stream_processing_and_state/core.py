from typing import Callable, Dict, Iterator, List, Optional, Any
import functools

from typesp import StringProcessorFn, StreamProcessorFn

def adapt_string_processor(processor_fn: StringProcessorFn) -> StreamProcessorFn:
    """
    Adapt a string processor (str -> str) to a stream processor (Iterator[str] -> Iterator[str]).
    
    Args:
        processor_fn: A function that processes a single string
        
    Returns:
        A function that processes a stream of strings
    """
    @functools.wraps(processor_fn)
    def stream_processor(lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            yield processor_fn(line)
    
    return stream_processor

def process_stream(lines: Iterator[str], processors: List[StreamProcessorFn]) -> Iterator[str]:
    """
    Process a stream of lines through a pipeline of processors.
    
    Args:
        lines: An iterator of input lines
        processors: A list of stream processor functions
        
    Returns:
        An iterator of processed lines
    """
    result = lines
    for processor in processors:
        result = processor(result)
    return result

class LineCounter:
    """A processor that adds a line number prefix to each line."""
    
    def __init__(self, start: int = 1, prefix: str = "[{line_num}] "):
        """
        Initialize the line counter.
        
        Args:
            start: The starting line number
            prefix: The format string for the line number prefix
        """
        self.line_num = start
        self.prefix = prefix
    
    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        """Process the input lines, adding line numbers."""
        for line in lines:
            yield self.prefix.format(line_num=self.line_num) + line
            self.line_num += 1

class LineSplitter:
    """A processor that splits lines on a delimiter and emits multiple lines."""
    
    def __init__(self, delimiter: str = ","):
        """
        Initialize the line splitter.
        
        Args:
            delimiter: The delimiter to split on
        """
        self.delimiter = delimiter
    
    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        """Process the input lines, splitting each one into multiple lines."""
        for line in lines:
            for part in line.split(self.delimiter):
                if part.strip():  # Skip empty parts
                    yield part.strip()

class LineJoiner:
    """A processor that joins pairs of lines into single lines."""
    
    def __init__(self, separator: str = " | "):
        """
        Initialize the line joiner.
        
        Args:
            separator: The separator to use when joining lines
        """
        self.separator = separator
        self.buffer: Optional[str] = None
    
    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        """Process the input lines, joining pairs of lines."""
        for line in lines:
            if self.buffer is None:
                self.buffer = line
            else:
                yield self.buffer + self.separator + line
                self.buffer = None
        
        # Don't forget the last line if there's an odd number
        if self.buffer is not None:
            yield self.buffer
            self.buffer = None
