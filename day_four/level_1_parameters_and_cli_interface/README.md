
# 🧾 Text Processing Script — Level 1

**Author:** ANURAG  
**Level:** 1 — Parameters and CLI Interface  
**Filename:** `process.py`  

## 📌 Description

This version builds upon the Level 0 script by introducing **command-line flexibility**, **environment defaults**, and **function-level structure** using the [`typer`](https://typer.tiangolo.com/) library.

The script processes an input text file line-by-line and applies configurable transformations such as `uppercase` or `snakecase`. Output can be printed to the console or saved to a specified file.


## 🚀 Features

- 🧩 **Command-line interface** using `typer`
- ⚙️ **.env support** for environment-based configuration (via `python-dotenv`)
- 🧱 **Two processing modes**:
  - `uppercase`: Converts lines to uppercase
  - `snakecase`: Replaces spaces with underscores and converts to lowercase
- 📂 **Flexible I/O**: Accept input and output paths via CLI


## 📁 File Structure

```

level_1_parameters_and_cli_interface/
├── process.py         # Main CLI script
├── .env               # Contains default mode configuration
├── input.txt          # Sample input file
├── uppercase.txt      # Expected output with uppercase mode
├── snakecase.txt      # Expected output with snakecase mode
├── output.txt         # Custom output file (generated)
└── README.md          # Documentation

```



## ⚙️ Setup

### 1. Install Dependencies

```
pip install typer[all] python-dotenv
````

### 2. Configure `.env`

```
# Default configuration for the text processor
MODE=uppercase
```

---

## ▶️ Usage

### Basic Usage

```
python process.py --input input.txt
```

This uses `MODE` from `.env` (default: `uppercase`).

### Specify Mode

```
python process.py --input input.txt --mode snakecase
```

### Redirect Output to File

```
python process.py --input input.txt --output output.txt
```

You can also combine:

```
python process.py --input input.txt --output output.txt --mode snakecase
```



## 🔄 Supported Modes

| Mode        | Description                          | Example Input | Output    |
| ----------- | ------------------------------------ | ------------- | --------- |
| `uppercase` | Converts text to all uppercase       | `hEy you`     | `HEY YOU` |
| `snakecase` | Replaces spaces with `_`, lowercases | `hEy you`     | `hey_you` |



## 🧠 Code Overview

All logic resides in `process.py`, broken into simple functions:

* `read_lines(path: str) -> Iterator[str]`
* `transform_line(line: str, mode: str) -> str`
* `write_output(lines: Iterator[str], output_path: Optional[str]) -> None`

These make the script clean, testable, and easy to extend in the next level.


## ✅ Checklist

* ✅ Accepts `--input` as a required argument
* ✅ Reads `--mode` from CLI or `.env`
* ✅ Supports both `uppercase` and `snakecase` modes
* ✅ Writes to stdout or file via `--output`
* ✅ CLI interface implemented with `typer`
* ✅ Logic cleanly broken into small functions


