import typer
from pathlib import Path

# Initialize the Typer CLI application
app = typer.Typer()

@app.command()
def process(
    input: Path = typer.Option(..., "--input", help="Input file"),
    output: Path = typer.Option(None, "--output", help="Output file"),
    config: Path = typer.Option(..., "--config", help="Path to pipeline.yaml")
):
    """
    Process a text file using a custom pipeline defined in a YAML config.

    This command reads lines from the input file, applies a sequence of
    transformations (defined in the pipeline YAML config), and writes the
    transformed lines to the output file if specified. Otherwise, it prints
    the output to the console.

    Parameters:
        input (Path): Path to the input text file.
        output (Path, optional): Path to the output file. If not provided, output is printed to stdout.
        config (Path): Path to the pipeline configuration YAML file.

    Example:
        $ python app.py process --input data.txt --config pipeline.yaml --output result.txt
    """
    # Import core logic here to keep CLI startup fast
    from core import apply_pipeline
    from pipeline import load_pipeline

    # Load transformation pipeline based on YAML config
    processors = load_pipeline(str(config))

    # Open input file for reading
    with open(input, "r") as f:
        # Create a generator of lines from the file
        lines = (line for line in f)

        # Apply the pipeline of processors to the lines
        transformed = apply_pipeline(lines, processors)

        if output:
            # If output path is given, write transformed lines to the file
            with open(output, "w") as out:
                for line in transformed:
                    out.write(line + "\n")
        else:
            # Otherwise, print transformed lines to console
            for line in transformed:
                print(line)
