# Level 0: Basic Script (No Abstraction)

This is the starting point of our journey - a simple, single-purpose script with no abstraction.

## 📝 Task

The script in this directory:

- Reads stdin line by line
- Strips leading and trailing whitespace from each line
- Converts the result to uppercase
- Prints the processed lines to stdout

## 📋 Implementation

The implementation is in a single file named `process.py` with no functions or modules - just sequential, top-to-bottom code.

## 🔍 Key Constraints

- No functions or abstractions
- Only Python built-in tools
- Sequential, procedural code

## 🚀 Usage

\`\`\`bash
cat input.txt | python process.py > output.txt
\`\`\`

## ✅ Checklist

- [ ] Script produces expected output for sample files
- [ ] Runs without errors from the command line
- [ ] No premature abstractions or refactoring

## 🔄 Next Steps

In the next level, we'll add parameters and a CLI interface to make this script more flexible and reusable.
