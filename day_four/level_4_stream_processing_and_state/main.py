from typing import Iterator, Optional

from core import process_stream
from pipeline import load_pipeline_from_config

def read_lines(path: str) -> Iterator[str]:
    """Read lines from a file."""
    with open(path, 'r') as file:
        for line in file:
            yield line.strip()

def write_output(lines: Iterator[str], output_path: Optional[str]) -> None:
    """Write lines to the specified output or stdout."""
    if output_path:
        with open(output_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')
    else:
        for line in lines:
            print(line)

def run_pipeline(input_path: str, output_path: Optional[str], config_path: str) -> None:
    """Run the processing pipeline on the input file."""
    # Load the pipeline from the configuration file
    processors = load_pipeline_from_config(config_path)
    
    # Read, process, and write
    lines = read_lines(input_path)
    processed_lines = process_stream(lines, processors)
    write_output(processed_lines, output_path)

if __name__ == "__main__":
    from cli import run_cli
    run_cli()
