

# 🚰 Text Processor – Level 4: Stream-Based Processing & Stateful Pipelines

> Author: **ANURAG**

A powerful and extensible text transformation pipeline that processes text as a stream of lines. This level introduces stream-aware processors, enabling dynamic fan-in, fan-out, and stateful behaviors like counting or buffering — all driven by the same dynamic `pipeline.yaml`.



## 📁 Project Structure

```
level_4_stream_processing_and_state/
├── main.py                  # Entry point
├── cli.py                   # Typer-based CLI interface
├── core.py                  # Core streaming pipeline engine
├── pipeline.py              # Dynamic pipeline loader from YAML
├── types.py                 # StreamProcessorFn type definitions
├── pipeline.yaml            # YAML config defining processing steps
└── processors/
    ├── upper.py             # Reuses str -> str to_uppercase
    ├── snake.py             # Reuses str -> str to_snakecase
    ├── fanout_splitter.py   # Stream-based fan-out processor (split by space)
    └── stateful_counter.py  # Stream-based stateful processor (line counter)
```


## ⚙️ Features

✅ Dynamic processor configuration via `pipeline.yaml`
✅ Stream-based processor interface: `Iterator[str] -> Iterator[str]`
✅ Backward compatibility with `str -> str` processors
✅ Support for fan-out (split lines), fan-in (combine lines), and stateful logic
✅ Cleanly wrapped function decorators for legacy processor reuse
✅ Easy extension via class-based processors with configuration



## 📌 Installation

```
pip install typer[all] pyyaml
```

---

## 🧪 Example Usage

```
python main.py --input input.txt --config pipeline.yaml
```

Or with output:

```
python main.py --input input.txt --config pipeline.yaml --output result.txt
```

---

## 🧱 YAML Pipeline Example

```
pipeline:
  - type: processors.stateful_counter.LineCounter
  - type: processors.upper.to_uppercase
  - type: processors.fanout_splitter.SplitLines
```

This pipeline:

1. Adds line numbers (stateful)
2. Converts to uppercase
3. Splits each line by spaces (fan-out)


## 🔁 Stream Processor Signature

```
# types.py
StreamProcessorFn = Callable[[Iterator[str]], Iterator[str]]
```

All processors now operate on streams of lines, enabling more powerful transformations.

To reuse old `str -> str` processors:

```
def str_to_stream(fn: Callable[[str], str]) -> StreamProcessorFn:
    def wrapped(lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            yield fn(line)
    return wrapped
```


## 📂 Sample Processors

### ✅ Legacy str -> str (wrapped for streaming)

**processors/upper.py**

```
def to_uppercase(line: str) -> str:
    return line.strip().upper()
```

### 🔄 Fan-out Processor

**processors/fanout\_splitter.py**

```
class SplitLines:
    def __init__(self, delimiter=" "):
        self.delimiter = delimiter

    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            yield from line.strip().split(self.delimiter)
```

### 🔢 Stateful Processor

**processors/stateful\_counter.py**

```
class LineCounter:
    def __init__(self):
        self.count = 0

    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            self.count += 1
            yield f"LINE {self.count}:\n{line.strip()}"
```



## 📥 Input / Output Examples

| Input (`input.txt`)      | Pipeline Steps                      | Output Lines                                         |
| ------------------------ | ----------------------------------- | ---------------------------------------------------- |
| `Hello World`            | LineCounter → to\_uppercase → Split | `LINE 1:`<br>`HELLO`<br>`WORLD`                      |
| `Python is Surely gREAt` | LineCounter → to\_uppercase → Split | `LINE 2:`<br>`PYTHON`<br>`IS`<br>`SURELY`<br>`GREAT` |
| `PiplInes Are GoOd`      | LineCounter → to\_uppercase → Split | `LINE 3:`<br>`PIPLINES`<br>`ARE`<br>`GOOD`           |



## 🧯 Error Handling

If a processor path is invalid or cannot be loaded:

```
ImportError: Could not load processor processors.fake.module: No module named 'processors.fake'
```

The system will give a clear traceback to guide you.

---

## 🧠 Advanced Behavior Supported

* ✅ Emit 0, 1, or many lines from 1 input (fan-out/fan-in)
* ✅ Maintain internal state across lines (e.g., line counter)
* ✅ Configure processors at initialization (via class params)
* ✅ Seamless fallback to function-based legacy processors

---

## 🧩 Extending with New Processors

1. Create a new file under `processors/`
2. Define a class with `__init__` and `__call__(self, lines: Iterator[str])`
3. Add to your `pipeline.yaml` using its full import path:

```
pipeline:
  - type: processors.my_processor.MyClass
```

---

## ✅ Checklist

* [x] Supports streaming processors (`Iterator[str] -> Iterator[str]`)
* [x] Reuses existing `str -> str` processors
* [x] Introduces fan-out and stateful processing
* [x] Clean class-based design with configuration support
* [x] Pipeline.yaml remains unchanged from Level 3


## 📜 License

MIT License
