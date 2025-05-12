# 📁 Automated Folder Monitor and Recovery - Level 8
**Author:** ANURAG

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0+-green.svg)](https://fastapi.tiangolo.com/)

## 📋 Description

A robust, self-running, fault-tolerant file processing tool that continuously monitors folders for new files, processes them through a configurable pipeline, and automatically recovers from failures. This system implements a persistent, observable, recoverable processing loop that runs autonomously and maintains processing state even through crashes or restarts.

## 🎯 Motivation

Modern data processing systems need to handle files that arrive at unpredictable times:
- 📊 Log files from various applications
- 💼 Transaction batches from business systems
- 📤 User uploads and data submissions

This system addresses these needs with a **persistent, observable, recoverable processing loop** that runs autonomously and maintains processing state even through crashes or restarts.

## ✨ Features

- **🔄 Continuous Folder Monitoring**: Automatically detects and processes new files
- **🛠️ Configurable Processing Pipeline**: Apply multiple transformations to your data
- **🛡️ Fault Tolerance & Recovery**: Resumes interrupted work after crashes
- **📊 Real-time Web Dashboard**: Monitor system status, metrics, and file processing
- **👁️ Observability**: Comprehensive metrics and traces for debugging
- **🔒 Thread Safety**: Properly handles concurrent operations

## 📥 Installation

```bash
# Clone the repository
git clone https://github.com/ANURAGJAMANKAR/bootcamp.git
cd AganithaBootcamp/day_four/level_8_automated_folder_monitor_and_recovery

# Install dependencies
pip install fastapi uvicorn
```

## 📂 Folder Structure

The system uses a folder-based queue with the following structure:

```
watch_dir/
├── unprocessed/     # incoming files to watch 
├── underprocess/    # in-progress files
├── processed/       # completed successfully
```

## 🚀 Usage

### Monitor a folder for files

```bash
python main.py --monitor ./watch_dir --trace --dashboard
```

### Monitor with custom output directory

```bash
python main.py --monitor ./watch_dir --output-dir ./results --trace --dashboard
```

### Use a custom configuration

```bash
python main.py --monitor ./watch_dir --config pipeline_config.json --trace --dashboard
```

### Process a single file (still supported)

```bash
python main.py --file input.txt --output result.txt --trace --dashboard
```

## 🔄 File Lifecycle

1. Files are placed in the `unprocessed/` directory
2. The system moves them to `underprocess/` while processing
3. After successful processing, files are moved to `processed/`
4. If the system crashes during processing, files in `underprocess/` are moved back to `unprocessed/` on restart

## 🏗️ Architecture

### Core Components

- **FolderMonitor**: Watches for new files and manages the processing lifecycle
- **MetricsStore**: Singleton for storing metrics, traces, and file statistics
- **ObservableProcessor**: Base class for processors that collect metrics
- **Dashboard**: FastAPI web server for monitoring
- **ObservablePipeline**: Chains processors together

### Project Structure

```
level_8_automated_folder_monitor_and_recovery/
├── README.md
├── metrics/
│   ├── __init__.py
│   ├── metrics_store.py       # Metrics collection and storage
│   └── tracer.py              # Tracing functionality
├── processors/
│   ├── __init__.py
│   ├── base.py                # Base processor classes
│   ├── simple.py              # Simple processors (uppercase, filter, etc.)
│   └── stateful.py            # Stateful processors (counter, aggregator)
├── pipeline/
│   ├── __init__.py
│   └── pipeline.py            # Pipeline implementation
├── dashboard/
│   ├── __init__.py
│   └── server.py              # Web dashboard
├── config/
│   ├── __init__.py
│   └── config_loader.py       # Configuration handling
├── folder_monitor/
│   ├── __init__.py
│   └── file_processor.py      # Folder monitoring implementation
└── main.py                    # Entry point
```

### Recovery Mechanism

The system implements a robust recovery mechanism:

1. On startup, it checks for any files in the `underprocess/` directory
2. These files are moved back to `unprocessed/` for reprocessing
3. This ensures that no files are lost if the system crashes during processing

## 📊 Dashboard

### Dashboard Visualization

Below are screenshots of the dashboard in action:

#### Main Dashboard - Continuous File Processing
![Dashboard Overview](/day_four/level_8_automated_folder_monitor_and_recovery/dashboard_visuals/Continuous_File_Processing.png)
*The main dashboard shows a complete overview of the system with summary metrics*

#### Main Dashboard - Process Monitor
![Dashboard Overview](/day_four/level_8_automated_folder_monitor_and_recovery/dashboard_visuals/Process_Monitor.png)
*The main dashboard shows a complete overview of the system with summary metrics*


The web dashboard is available at [http://localhost:8000](http://localhost:8000) when enabled with the `--dashboard` flag.

The dashboard includes:

- **File Processing Status**:
  - Number of files in each directory
  - Currently processing file
  - Recently processed files with timestamps
- **Processor Metrics**: Lines in/out, processing time, and error counts
- **Traces**: The path of lines through the system (when enabled with `--trace`)
- **Errors**: Recent errors with processor information

## ⚙️ Configuration

You can configure processors using a JSON file:

```json
{
  "processors": [
    {
      "type": "line_counter",
      "id": "counter",
      "format": "Line {count}: {line}"
    },
    {
      "type": "uppercase",
      "id": "uppercase"
    },
    {
      "type": "filter",
      "id": "important_filter",
      "pattern": "important"
    }
  ]
}
```

## 🧠 Design Considerations

- **Thread Safety**: All shared data is protected by locks to ensure thread safety
- **Non-Blocking**: The processing loop doesn't block the main thread
- **Idempotency**: The system assumes reprocessing files is harmless
- **Atomic File Operations**: Uses `shutil.move()` for safe file transitions

## 💭 Reflection

### Concurrent Instances

If two instances of this system run at once:
- They might try to process the same files
- This could lead to race conditions and duplicate processing
- Solutions include:
  - File locking mechanisms
  - A distributed lock manager
  - Assigning different files to different instances based on naming patterns

### Parallelization

To parallelize processing across threads or nodes:
- We could use a thread pool to process multiple files concurrently
- Each thread would need its own set of processors to avoid state conflicts
- A work queue could distribute files to worker threads/nodes
- Each worker would need its own `underprocess` directory

### Partial Files

If a file is only partially written when picked up:
- The system might process incomplete data
- Solutions include:
  - Using file locks during writing
  - Implementing a "ready" flag (e.g., a companion .ready file)
  - Checking file modification time and only processing files that haven't been modified for a certain period
  - Using atomic file operations (write to temp file, then rename)

## 🔮 Next Steps

Future improvements could include:
- Implementing more sophisticated error handling and retry mechanisms
- Adding support for different file formats and schemas
- Implementing a more advanced routing system
- Adding support for distributed processing across multiple machines

## ✅ Checklist

- [ ] System continuously monitors the `unprocessed/` directory
- [ ] Files are safely moved through the processing lifecycle
- [ ] Failed or interrupted files are retried automatically on restart
- [ ] Processing loop is non-blocking and resilient
- [ ] Web dashboard updates live with file state and statistics
- [ ] System can run indefinitely without manual intervention
- [ ] Error handling properly manages exceptions
- [ ] Configuration is flexible and easily modifiable
- [ ] Metrics provide useful insights into system performance

## 📄 License

MIT License

Copyright (c) 2025 ANURAG

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
