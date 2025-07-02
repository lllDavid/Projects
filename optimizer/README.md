# Optimizer

![Project Status](https://img.shields.io/badge/status-early%20development-orange)

- A tool for identifying performance bottlenecks in Python functions, benchmarking and profiling them, and converting selected code into optimized Cython for improved execution speed.

## Features
### Implemented
Currently all features are limited to a **hardcoded** example function.

- Converts a **hardcoded** Python function into a .pyx module for performance optimization.

- **Benchmark:** Compares execution times of the original and optimized function.
 
- **Bottleneck Analysis:**  Analyzes execution times of each line to identify performance bottlenecks.

- **Line-by-Line Profiling Report:** Outputs detailed profiling statistics using line_profiler.

### Planned
- More dynamic workflow, use module provided by user and automatically improve it using:
- **Dynamic Type Tracing:** Collect runtime types of arguments, locals, and return values using tracing.
- **Cython Code Generation**: Use collected types to convert the Python function into a Cython module. (Currently, this process generates a basic .pyx file without full Cython features like cdef declarations or advanced optimizations.)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/lllDavid/optimizer
```

### 2. Install dependencies

**Navigate to the directory:**
```bash
cd optimizer
```

**Create a virtual environment:**
```bash
python -m venv venv
```


**Activate the virtual environment:**
```bash
.\venv\Scripts\activate
```


**Install requirements:**
```bash
pip install -r requirements.txt
```


### 3. Run the Application

```bash
python main.py
```