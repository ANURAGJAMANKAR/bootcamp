from typing import Callable, Dict, Iterator, List, Any, Protocol, TypeVar

# Define the old processor function type
StringProcessorFn = Callable[[str], str]

# Define the new stream processor function type
StreamProcessorFn = Callable[[Iterator[str]], Iterator[str]]

# Define a type for a list of stream processors
StreamProcessorList = List[StreamProcessorFn]

# Define a type for the pipeline configuration
PipelineConfig = Dict[str, List[Dict[str, Any]]]

# Define a Protocol for processors with configuration
class ConfigurableProcessor(Protocol):
    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        ...

T = TypeVar('T')
