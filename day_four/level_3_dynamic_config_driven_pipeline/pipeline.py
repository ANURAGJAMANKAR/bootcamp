import yaml
import importlib
from processor_types import ProcessorFn

def load_pipeline(config_path: str) -> list[ProcessorFn]:
    """
    Load a processing pipeline from a YAML configuration file.

    This function reads a YAML file that defines a sequence of processor
    functions. Each processor is dynamically imported using its full
    dotted path (e.g., "processors.text.strip_whitespace") and collected
    into a list. These processors are expected to conform to the `ProcessorFn`
    type (i.e., they accept and return a string).

    Parameters:
        config_path (str): Path to the YAML configuration file.

    Returns:
        list[ProcessorFn]: A list of callable processor functions in the
                           order they appear in the config.

    YAML Config Format Example:
    ```yaml
    pipeline:
      - type: processors.text.strip_whitespace
      - type: processors.text.to_uppercase
    ```

    Raises:
        ImportError: If a module or function cannot be found or imported.
    """
    # Open and parse the YAML config
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    # Extract the 'pipeline' list from the config (or empty list if missing)
    steps = config.get("pipeline", [])
    processors = []

    # Dynamically import each processor function by its dotted path
    for step in steps:
        path = step["type"]
        module_path, func_name = path.rsplit(".", 1)
        try:
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
            processors.append(func)
        except (ModuleNotFoundError, AttributeError) as e:
            raise ImportError(f"Could not load processor {path}: {e}")

    return processors
