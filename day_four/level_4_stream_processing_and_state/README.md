# Level 4: Stream Processing and State

In this level, we move from simple string-to-string functions to full stream-based processing, enabling more powerful behaviors like fan-out, fan-in, and stateful processing.

## 📝 Task

The code in this directory:

- Redesigns the processor interface to be `Iterator[str] -> Iterator[str]`
- Provides a wrapper to adapt existing str -> str processors
- Implements stateful processors that maintain internal state
- Supports processors that can emit multiple lines from one input (fan-out)
- Supports processors that can combine multiple lines into one output (fan-in)

## 🧩 Key Concepts

- Stream-based processing
- Stateful processors
- Fan-out and fan-in operations
- Processor initialization with configuration
- Class-based processors

## 📋 New Processor Types

- **LineCounter**: Adds a line number prefix to each line
- **LineSplitter**: Splits lines on a delimiter and emits multiple lines
- **LineJoiner**: Joins pairs of lines into single lines

## 🚀 Usage

\`\`\`bash
python main.py --input input.txt --config pipeline.yaml
\`\`\`

## ✅ Checklist

- [ ] All processors support `Iterator[str] -> Iterator[str]` interface
- [ ] System can reuse str -> str functions via a wrapper
- [ ] At least one processor emits more or fewer lines than it receives
- [ ] At least one processor maintains internal state
- [ ] Clean way to pass configuration to processors during initialization
- [ ] Stream processors are testable in isolation

## 🔄 Next Steps

In the next level, we'll build a DAG-based processing engine where each line can take a different path through the system based on its content or tags.
