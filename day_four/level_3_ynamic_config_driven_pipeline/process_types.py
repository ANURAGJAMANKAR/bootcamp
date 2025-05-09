from typing import Callable, Dict, List, Any

# Define the processor function type
ProcessorFn = Callable[[str], str]

# Define a type for a list of processors
ProcessorList = List[ProcessorFn]

# Define a type for the pipeline configuration
PipelineConfig = Dict[str, List[Dict[str, Any]]]
