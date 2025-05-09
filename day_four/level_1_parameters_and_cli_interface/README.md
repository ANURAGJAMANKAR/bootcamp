# Level 1: Parameters and CLI Interface

In this level, we transform our one-off script into a basic parameterized tool.

## 📝 Task

The script in this directory:

- Uses `typer` to define a command-line interface
- Accepts input file path, output file path, and processing mode
- Loads default values from a `.env` file
- Implements different processing behaviors based on the mode

## 🔄 Supported Modes

- `uppercase`: Convert each line to uppercase
- `snakecase`: Replace spaces with underscores and convert to lowercase

## 🧩 Key Concepts

- Command-line arguments
- Environment defaults
- Functional decomposition

## 🚀 Usage

\`\`\`bash
# Using default mode from .env
python process.py --input input.txt

# Specifying mode
python process.py --input input.txt --mode snakecase

# Default output file
python process.py --input uppercase.txt --output output.txt

# Specifying output file
python process.py --input input.txt --mode snakecase --output snakecase.txt
\`\`\`

## ✅ Checklist

- [ ] Script processes files passed via `--input`
- [ ] Default mode is loaded from `.env`
- [ ] Different modes produce different transformations
- [ ] Results can be printed to stdout or written to file
- [ ] Clean CLI using typer
- [ ] Logic divided into small functions

## 🔄 Next Steps

In the next level, we'll extract these functions into separate modules for better organization and maintainability.
