# Level 2: Modular Structure and Standardized Processing

In this level, we convert our working CLI script into a structured program with clearly separated responsibilities.

## 📝 Task

The code in this directory is split into multiple modules:

- `main.py`: Reads input, writes output
- `cli.py`: Handles CLI via typer
- `core.py`: Applies a list of processors to each line
- `pipeline.py`: Assembles the processor list based on mode
- `types.py`: Defines ProcessorFn types

## 🧩 Key Concepts

- Modular code organization
- Separation of concerns
- Standard processor interface
- Function composition

## 📋 Module Responsibilities

- **main.py**: Orchestrates the overall process flow
- **cli.py**: Handles command-line arguments and options
- **core.py**: Contains the core processing functions
- **pipeline.py**: Builds the processing pipeline based on mode
- **types.py**: Defines common types used across modules

## 🚀 Usage

\`\`\`bash
python main.py --input input.txt --output output.txt --mode uppercase
\`\`\`

## ✅ Checklist

- [ ] Code is organized into 5 separate modules
- [ ] Processor type `ProcessorFn = Callable[[str], str]` is used consistently
- [ ] New processors can be added without changing main logic
- [ ] Pipeline is a list of functions composed over each line
- [ ] CLI behavior works correctly via Typer
- [ ] No circular imports

## 🔄 Next Steps

In the next level, we'll introduce dynamic configuration and support for chaining multiple processors via configuration files.
