# API Reference

This page documents the public API of the `anurag-hello` package.

## Core Module

### say_hello

```
def say_hello(name: str = "World") -> str:
    """
    Returns a greeting message for the given name.
    
    Args:
        name: The name to greet. Defaults to "World".
        
    Returns:
        A greeting string.
    """
```


**Example:**

```
from anurag_hello import print_rich_hello

# Default greeting with rich formatting
print_rich_hello()  # Displays: Hello, World! in a fancy panel

# Custom greeting with rich formatting
print_rich_hello("Anurag")  # Displays: Hello, Anurag! in a fancy panel
```

## CLI Module

The CLI module is not typically imported directly but is used through the command-line interface.

### hello command

```
anurag-hello hello [NAME]
```

Prints a rich formatted greeting message. If no name is provided, it will greet the world.

**Arguments:**

- `NAME`: Optional. The name to greet.


**Example:**
```
anurag-hello hello
anurag-hello hello Anurag

```

### simple command

```

anurag-hello simple [NAME]

```

Prints a simple greeting message without rich formatting. If no name is provided, it will greet the world.

**Arguments:**
- `NAME`: Optional. The name to greet.

**Example:**
```
anurag-hello simple
anurag-hello simple Anurag
```

## Internal Structure

The package is structured as follows:

```
anurag_hello/
├── __init__.py      # Exports say_hello and print_rich_hello
├── main.py          # Contains core functionality
└── cli.py           # Implements the command-line interface
```

The `__init__.py` file exports the main functions:

```
from .main import say_hello, print_rich_hello

__all__ = ["say_hello", "print_rich_hello"]
```

This means you can import these functions directly from the package:

```
from anurag_hello import say_hello, print_rich_hello
```