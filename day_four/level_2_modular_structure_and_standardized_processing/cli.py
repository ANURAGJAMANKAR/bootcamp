import typer
from dotenv import load_dotenv
import os
from core import read_lines, write_output, process_lines
from pipeline import build_pipeline

load_dotenv()
app = typer.Typer()

@app.command()
def run(
    input: str = typer.Option(..., "--input", "-i", help="Input file path"),
    output: str = typer.Option(None, "--output", "-o", help="Output file path"),
    mode: str = typer.Option(None, "--mode", "-m", help="Processing mode")
):
    mode = mode or os.getenv("MODE", "uppercase")
    lines = read_lines(input)
    processors = build_pipeline(mode)
    processed = process_lines(lines, processors)
    write_output(processed, output)
