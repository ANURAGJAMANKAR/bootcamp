
# 🧾 Text Processing CLI — Level 2: Modular Structure & Composable Pipelines

**Author:** ANURAG  
**Level:** 2 — Modular Architecture & Functional Composition  


## 📌 Description

This version introduces a cleanly **modularized structure** and a **composable processing pipeline**. The application is now organized into reusable components with a common processor interface, enabling transformations like `uppercase`, `snakecase`, and more — all assembled dynamically at runtime.



## 📂 Project Structure

```

level_2_modular_structure_and_standardized_processing/
├── main.py         # Entrypoint – calls CLI
├── cli.py          # Command-line interface (Typer)
├── core.py         # Core logic: reading, writing, processors
├── pipeline.py     # Builds a processor pipeline based on mode
├── process\_types.py# Shared processor function type
├── .env            # Default configuration
├── input.txt       # Example input
├── snakecase.txt   # Sample output: snake\_case mode
├── uppercase.txt   # Sample output: UPPERCASE mode
└── both.txt        # Potential output for extended pipeline

```



## ⚙️ Setup

### 1. Install Dependencies

```
pip install typer[all] python-dotenv
````

### 2. Create `.env`

```
# .env
MODE=uppercase
```

---

## ▶️ Usage

Run via the `main.py` entrypoint:

```
python main.py run --input input.txt
```

Optional arguments:

```
python main.py run --input input.txt --output output.txt --mode snakecase

python main.py --input input.txt --output output.txt --mode uppercase

```

Flags:

* `--input` / `-i`: Required path to input file
* `--output` / `-o`: Optional path for output file (defaults to stdout)
* `--mode` / `-m`: Processing mode (default from `.env`)


## 🔄 Supported Modes

| Mode        | Description                                     | Example Input | Output      |
| ----------- | ----------------------------------------------- | ------------- | ----------- |
| `uppercase` | Converts lines to uppercase                     | `i love py`   | `I LOVE PY` |
| `snakecase` | Replaces spaces with underscores and lowercases | `i love py`   | `i_love_py` |

More modes can be added by simply creating new processor functions in `core.py` and including them in `pipeline.py`.


## 🧠 Code Overview

### 🔧 Processor Type

```
# process_types.py
ProcessorFn = Callable[[str], str]
```

### 🧱 Core Logic (`core.py`)

* `to_uppercase(line: str) -> str`
* `to_snakecase(line: str) -> str`
* `read_lines(path)`: Reads input line-by-line
* `process_lines(lines, processors)`: Applies all processors in sequence
* `write_output(...)`: Outputs to file or stdout

### 🧪 Pipeline Builder (`pipeline.py`)

```
def build_pipeline(mode: str) -> list[ProcessorFn]:
    ...
```

Returns a list of processing functions based on the selected mode.



## ✅ Checklist

* ✅ Follows modular architecture (5 files)
* ✅ Defines and uses `ProcessorFn = Callable[[str], str]`
* ✅ CLI still works identically to Level 1
* ✅ Easy to add new processors without touching core logic
* ✅ Avoids circular imports using `process_types.py`
* ✅ Composable function pipeline

