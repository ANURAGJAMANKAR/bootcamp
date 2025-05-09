import importlib
import yaml
from typing import Any, Dict, List, Type, Union, Callable

from typesp import StreamProcessorFn, StreamProcessorList, ConfigurableProcessor
from core import adapt_string_processor

def load_processor(config: Dict[str, Any]) -> StreamProcessorFn:
    """
    Dynamically load a processor from its configuration.
    
    Args:
        config: The processor configuration
        
    Returns:
        The loaded processor function
    
    Raises:
        ImportError: If the module or function cannot be imported
        TypeError: If the imported object is not callable
    """
    import_path = config['type']
    
    try:
        module_path, object_name = import_path.rsplit('.', 1)
        module = importlib.import_module(module_path)
        processor_class_or_fn = getattr(module, object_name)
        
        if not callable(processor_class_or_fn):
            raise TypeError(f"Imported object '{import_path}' is not callable")
        
        # Check if it's a class or a function
        if isinstance(processor_class_or_fn, type):
            # It's a class, instantiate it with any provided parameters
            params = config.get('params', {})
            processor_instance = processor_class_or_fn(**params)
            return processor_instance
        else:
            # It's a function, check if it's a string processor or stream processor
            if hasattr(processor_class_or_fn, '__annotations__') and \
               'return' in processor_class_or_fn.__annotations__ and \
               processor_class_or_fn.__annotations__['return'] == str:
                # It's a string processor, adapt it
                return adapt_string_processor(processor_class_or_fn)
            else:
                # Assume it's already a stream processor
                return processor_class_or_fn
    
    except (ImportError, AttributeError) as e:
        raise ImportError(f"Failed to import processor '{import_path}': {str(e)}")

def load_pipeline_from_config(config_path: str) -> StreamProcessorList:
    """
    Load a pipeline from a YAML configuration file.
    
    Args:
        config_path: Path to the YAML configuration file
        
    Returns:
        A list of stream processor functions
    """
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        
        validate_config(config)
        
        processors = []
        for step in config['pipeline']:
            processor = load_processor(step)
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
