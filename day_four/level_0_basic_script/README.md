# 🧾 Text Processing Script — Level 0

**Author:** ANURAG  
**Level:** 0 — Basic Script (No Abstraction)  
**Filename:** `process.py`  

## 📌 Description

This is a minimal, single-purpose Python script designed to perform basic text transformation from standard input (stdin) to standard output (stdout). It represents **Level 0** of an incremental software design journey, starting with a quick, unrefactored solution.

### 🔧 What it Does

The script:
- Reads input line-by-line from `stdin`
- Strips leading and trailing whitespace from each line
- Converts each cleaned line to **uppercase**
- Prints the result to `stdout`

## 📁 File Structure

```

level_0_basic_script
├── process.py     # The main script
├── input.txt      # (Optional) Sample input file
├── output.txt     # (Optional) Captured output
└── README.md      # Project documentation

````

## ▶️ Usage

### 1. Prepare your input file (optional):

```
echo "  hello world  " > input.txt
```

```
cat input.txt | python process.py > output.txt
```

### 2. Run the script from the command line:

```
python3 process.py < input.txt > output.txt
```

### 3. Check the output:

```
cat output.txt
# Output:
# HELLO WORLD
```

## ✅ Constraints

* No functions, classes, or abstractions — just top-to-bottom code.
* Only built-in Python modules allowed.
* Focused solely on behavior and correctness for now.

## 📋 Task Checklist

* ✅ Produces correct output for a sample file
* ✅ Runs without errors from the command line
* ✅ No refactoring or abstractions added yet

```

> This project is part of a progressive development exercise. Later levels will introduce refactoring, modularity, and testing.

```

