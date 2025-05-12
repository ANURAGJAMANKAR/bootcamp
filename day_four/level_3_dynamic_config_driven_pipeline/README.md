

# 🧠 Text Processor – Level 3: Dynamic Config-Driven Pipeline

> Author: **ANURAG**

A modular, extensible Python text transformation tool that reads text files line by line and applies customizable processing pipelines defined via a YAML config. Designed to evolve from simple scripting to a full plugin-ready architecture.



## 📁 Project Structure

```
level_3_dynamic_config_driven_pipeline/
├── main.py               # Entry point
├── cli.py                # CLI interface using Typer
├── core.py               # Applies processor pipeline
├── pipeline.py           # Loads dynamic processor pipeline from YAML
├── processor_types.py    # Shared type alias for processor functions
├── processors/           # Modular processor implementations
│   ├── upper.py          # UPPERCASE transformer
│   └── snake.py          # snake_case transformer
└── pipeline.yaml         # YAML config defining processor sequence
```



## ⚙️ Features

* ✅ Clean CLI interface using [Typer](https://typer.tiangolo.com/)
* ✅ Configurable pipeline via `pipeline.yaml`
* ✅ Dynamically loaded processing functions (imported at runtime)
* ✅ Supports chaining multiple transformations
* ✅ Prints to stdout or writes to output file
* ✅ Fully type-safe with `ProcessorFn = Callable[[str], str]`



## 📌 Installation

```
pip install typer[all] python-dotenv pyyaml
```



## 🧪 Example Usage

### Command-line execution:

```
python main.py --input input.txt --config pipeline.yaml
```

Or with output:

```
python main.py --input input.txt --config pipeline.yaml --output result.txt
```



## 🧱 YAML Pipeline Example

```
pipeline:
  - type: processors.snake.to_snakecase   # Converts to snake_case
  - type: processors.upper.to_uppercase   # Then converts to UPPERCASE
```

These functions will be applied in the given order for each line in the input file.



## 📝 Processor Function Signature

All processor functions conform to this type:

```python
# processor_types.py
ProcessorFn = Callable[[str], str]
```

This allows functions to be composed into a transformation pipeline like so:

```
def apply_pipeline(lines: Iterator[str], processors: list[ProcessorFn]) -> Iterator[str]:
    for line in lines:
        for processor in processors:
            line = processor(line)
        yield line
```



## 📂 Sample Processors

### processors/snake.py

```
def to_snakecase(line: str) -> str:
    return line.strip().lower().replace(" ", "_")
```

### processors/upper.py

```
def to_uppercase(line: str) -> str:
    return line.strip().upper()
```



## 📥 Input / Output Examples

| Input (`input.txt`) | YAML Pipeline                   | Output        |
| ------------------- | ------------------------------- | ------------- |
| `Hello World`       | `to_uppercase`                  | `HELLO WORLD` |
| `Hello World`       | `to_snakecase`                  | `hello_world` |
| `Hello World`       | `to_snakecase` → `to_uppercase` | `HELLO_WORLD` |
| `   hi  there   `   | `to_snakecase` → `to_uppercase` | `HI_THERE`    |



## 🧯 Error Handling

If a function path in the YAML config is invalid or missing:

```
ImportError: Could not load processor processors.bad.path: No module named 'processors.bad'
```

The app will raise a clear error so you can fix your `pipeline.yaml`.

---

## 💡 Extending the Pipeline

To add a new transformation:

1. Create a file in `processors/` (e.g., `reverse.py`)
2. Define a `str -> str` function:

```
def reverse(line: str) -> str:
    return line[::-1]
```

3. Add to `pipeline.yaml`:

```
pipeline:
  - type: processors.reverse.reverse
```

No need to change any other code.



## ✅ Checklist

* [x] CLI accepts `--config` YAML path
* [x] All processors follow `str -> str`
* [x] New processors added without modifying core logic
* [x] Uses dynamic imports for extensibility
* [x] Clean folder and type separation



## 📜 License

MIT License

