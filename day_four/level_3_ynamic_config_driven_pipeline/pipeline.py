import importlib
import yaml
from typing import Any, Dict, List

from process_types import ProcessorFn, ProcessorList, PipelineConfig

def load_processor(import_path: str) -> ProcessorFn:
    """
    Dynamically load a processor function from its import path.
    
    Args:
        import_path: Dotted import path to the processor function
        
    Returns:
        The loaded processor function
    
    Raises:
        ImportError: If the module or function cannot be imported
        TypeError: If the imported object is not callable
    """
    try:
        module_path, function_name = import_path.rsplit('.', 1)
        module = importlib.import_module(module_path)
        processor = getattr(module, function_name)
        
        if not callable(processor):
            raise TypeError(f"Imported object '{import_path}' is not callable")
        
        return processor
    except (ImportError, AttributeError) as e:
        raise ImportError(f"Failed to import processor '{import_path}': {str(e)}")

def load_pipeline_from_config(config_path: str) -> ProcessorList:
    """
    Load a pipeline from a YAML configuration file.
    
    Args:
        config_path: Path to the YAML configuration file
        
    Returns:
        A list of processor functions
    """
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        
        validate_config(config)
        
        processors = []
        for step in config['pipeline']:
            processor = load_processor(step['type'])
            processors.append(processor)
        
        return processors
    except Exception as e:
        raise ValueError(f"Failed to load pipeline from '{config_path}': {str(e)}")

def validate_config(config: Dict[str, Any]) -> None:
    """
    Validate the pipeline configuration.
    
    Args:
        config: The loaded configuration dictionary
        
    Raises:
        ValueError: If the configuration is invalid
    """
    if not isinstance(config, dict):
        raise ValueError("Configuration must be a dictionary")
    
    if 'pipeline' not in config:
        raise ValueError("Configuration must contain a 'pipeline' key")
    
    if not isinstance(config['pipeline'], list):
        raise ValueError("Pipeline must be a list")
    
    for i, step in enumerate(config['pipeline']):
        if not isinstance(step, dict):
            raise ValueError(f"Pipeline step {i} must be a dictionary")
        
        if 'type' not in step:
            raise ValueError(f"Pipeline step {i} must contain a 'type' key")
