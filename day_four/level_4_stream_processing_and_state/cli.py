from typing import Optional

import typer

app = typer.Typer()

@app.command()
def process(
    input: str = typer.Option(..., help="Input file path"),
    output: Optional[str] = typer.Option(None, help="Output file path (stdout if not specified)"),
    config: str = typer.Option("pipeline.yaml", help="Pipeline configuration file"),
):
    """Process a text file line by line using the pipeline defined in the config file."""
    from .main import run_pipeline
    
    run_pipeline(input, output, config)

def run_cli():
    """Run the CLI application."""
    app()
