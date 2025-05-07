# ⭐ anurag-hello

![PyPI Version](https://img.shields.io/badge/pypi-v0.3.0-blue)
![Python Versions](https://img.shields.io/badge/python-3.8%2B-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

A comprehensive Python package that demonstrates clean code principles through a simple "Hello World" application with rich formatting and a command-line interface.

## 📦 Installation

Install the latest version from TestPyPI:

```
pip install -i https://test.pypi.org/simple/ anurag-hello==0.3.0
```

## 🚀 Features

- ✅ Simple and intuitive API for greeting messages
- ✅ Rich text formatting for beautiful console output
- ✅ Command-line interface with multiple commands
- ✅ Type annotations for better IDE support and code quality
- ✅ Comprehensive documentation and examples
- ✅ Follows clean code principles and best practices

## 📋 Usage

### As a Library

```
# Basic usage
from anurag_hello import say_hello

# Simple greeting
result = say_hello()
print(result)  # Output: Hello, World!

# Greeting with a name
result = say_hello("Anurag")
print(result)  # Output: Hello, Anurag!

# Rich formatted greeting
from anurag_hello import print_rich_hello

print_rich_hello("Anurag")  # Displays a fancy greeting panel

```

### As a Command-Line Tool

```

# Display help information

anurag-hello --help

# Rich formatted greeting to the world

anurag-hello hello

# Rich formatted greeting to a specific person

anurag-hello hello Anurag

# Simple greeting without rich formatting

anurag-hello simple

# Simple greeting to a specific person

anurag-hello simple Anurag

```

## 📁 Project Structure

```

anurag-hello/
├── anurag_hello/
│   ├── **init**.py      # Package initialization and exports
│   ├── main.py          # Core functionality and rich formatting
│   └── cli.py           # Command-line interface implementation
├── pyproject.toml       # Project metadata and dependencies
├── README.md            # This documentation file
└── LICENSE              # MIT License file

```

## 📝 File Descriptions

### anurag_hello/\_\_init\_\_.py

Exports the main functions from the package for easy importing.

```
from .main import say_hello, print_rich_hello

__all__ = ["say_hello", "print_rich_hello"]
```

### anurag_hello/main.py

Contains the core functionality for generating greetings and rich-formatted output.

```
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Create a console instance
console = Console()

def say_hello(name: str = "World") -> str:
    """
    Returns a greeting message for the given name.
    
    Args:
        name: The name to greet. Defaults to "World".
        
    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"

def print_rich_hello(name: str = "World") -> None:
    """
    Prints a rich formatted greeting message.
    
    Args:
        name: The name to greet. Defaults to "World".
    """
    greeting = say_hello(name)
    text = Text(greeting, style="bold green")
    console.print(Panel(text, border_style="blue", title="Greeting"))

def main() -> None:
    """
    Main function that prints a rich greeting.
    """
    print_rich_hello()

if __name__ == "__main__":
    main()
```

### anurag_hello/cli.py

Implements the command-line interface using Typer.

```
import typer
from typing import Optional
from .main import print_rich_hello, say_hello

app = typer.Typer(help="A simple CLI application that says hello.")

@app.command()
def hello(name: Optional[str] = typer.Argument(None, help="The name to greet")):
    """
    Prints a rich formatted greeting message.
    
    If no name is provided, it will greet the world.
    """
    print_rich_hello(name if name else "World")

@app.command()
def simple(name: Optional[str] = typer.Argument(None, help="The name to greet")):
    """
    Prints a simple greeting message without rich formatting.
    
    If no name is provided, it will greet the world.
    """
    typer.echo(say_hello(name if name else "World"))

def main():
    """
    Entry point for the CLI application.
    """
    app()

if __name__ == "__main__":
    main()
```

### pyproject.toml

Project configuration file that defines metadata, dependencies, and entry points.

```
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "anurag-hello"
version = "0.3.0"
authors = [
    {name = "ANURAG JAMANKAR", email = "anurag.jamankar.aj@gmail.com"},
]
description = "This module provides a basic greeting functionality that takes a user's name and returns a personalized message. The output is enhanced using the rich library for better formatting, and the module is converted into a CLI tool using typer, enabling terminal-based interaction."
readme = "README.md"
requires-python = ">=3.13"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
    "rich>=13.0.0",
    "typer>=0.9.0",
]

[project.scripts]
anurag-hello = "anurag_hello.cli:main"

[project.urls]
"Homepage" = "https://github.com/ANURAGJAMANKAR/bootcamp/tree/183cdceaf439c47ba52c7e47690e72daab537402/day_zero"
```

## 🧪 Development Guide

This section walks through the development process for each exercise in the project.

### Exercise 1: Basic Setup

1. Initialize the project with `uv`:
```
mkdir anurag-hello
cd anurag-hello
uv init
```
2. Create a virtual environment:
```
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
3. Create the basic module structure:
```
mkdir anurag_hello
touch anurag_hello/**init**.py
touch anurag_hello/main.py
touch README.md
touch pyproject.toml
```
4. Implement the basic functionality in `main.py` and `__init__.py`
5. Configure `pyproject.toml` with project metadata
6. Build and publish to TestPyPI:
```
uv pip install build twine
python -m build
python -m twine upload --repository testpypi dist/*
```


### Exercise 2: Rich Formatting

1. Install the rich library:
```
uv pip install rich
```
2. Enhance the module to use rich formatting for console output
3. Update dependencies in `pyproject.toml`
4. Build and publish the updated package


### Exercise 3: Command-Line Interface

1. Install typer:
```
uv pip install typer
```
2. Create a CLI module (`cli.py`) with typer commands
3. Update `pyproject.toml` to include the CLI entry point
4. Build and publish the final package


## 📚 Learning Resources

- [Python Type Annotations](https://docs.python.org/3/library/typing.html)
- [Rich Documentation](https://rich.readthedocs.io/en/latest/)
- [Typer Documentation](https://typer.tiangolo.com/)
- [Python Packaging User Guide](https://packaging.python.org/en/latest/)
- [uv Package Manager](https://github.com/astral-sh/uv)


## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**ANURAG JAMANKAR**

- Email: [anurag.jamankar.aj@gmail.com](mailto:anurag.jamankar.aj@gmail.com)
- GitHub: [github.com/ANURAGJAMANKAR](https://github.com/ANURAGJAMANKAR)
- LinkedIn: [linkedin.com/in/anurag-jamankar](https://linkedin.com/in/anurag-jamankar)


