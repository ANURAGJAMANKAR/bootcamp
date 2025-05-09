#!/usr/bin/env python3
# Level 1: Parameters and CLI Interface
# This script processes text files with configurable modes and I/O options.

import os
import sys
from typing import Iterator, Optional

import typer
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create Typer app
app = typer.Typer()

def read_lines(path: str) -> Iterator[str]:
    """Read lines from a file."""
    with open(path, 'r') as file:
        for line in file:
            yield line.strip()

def transform_line(line: str, mode: str) -> str:
    """Transform a line based on the specified mode."""
    if mode == "uppercase":
        return line.upper()
    elif mode == "snakecase":
        return line.replace(" ", "_").lower()
    else:
        raise ValueError(f"Unknown mode: {mode}")

def write_output(lines: Iterator[str], output_path: Optional[str]) -> None:
    """Write lines to the specified output or stdout."""
    if output_path:
        with open(output_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')
    else:
        for line in lines:
            print(line)

@app.command()
def process(
    input: str = typer.Option(..., help="Input file path"),
    output: Optional[str] = typer.Option(None, help="Output file path (stdout if not specified)"),
    mode: Optional[str] = typer.Option(
        None, help="Processing mode: uppercase or snakecase"
    ),
):
    """Process a text file line by line with the specified mode."""
    # Use environment default if mode not specified
    if mode is None:
        mode = os.getenv("MODE", "uppercase")
    
    # Read, transform, and write
    lines = read_lines(input)
    transformed_lines = (transform_line(line, mode) for line in lines)
    write_output(transformed_lines, output)

if __name__ == "__main__":
    app()
