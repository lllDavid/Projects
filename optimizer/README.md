# Optimizer

![Project Status](https://img.shields.io/badge/status-early%20development-orange)

## Features:
- Converts a (currently)hardcoded Python function to Cython for optimization.

- Benchmark: Python vs. Cython – Compares execution times of the original and optimized function.
 
- Function Bottleneck Analysis – Analyzes execution times of each line to identify performance bottlenecks.

- Line-by-Line Profiling Report – Prints detailed profiling statistics using line_profiler.

## Usage

### Clone
```bash
git clone https://github.com/lllDavid/optimizer
```
### Change Directory
```bash
cd optimizer
```

### Install dependencies
#### Windows

##### Create venv
```bash
python -m venv venv
```

##### Activate venv
```bash
venv\Scripts\activate
```
##### Install
```bash
pip install -r requirements.txt
```

#### Linux
##### Create venv
```bash
python3 -m venv venv
```

##### Activate venv 
```bash
source venv/bin/activate
```

##### Install
```bash
pip install -r requirements.txt
```

### Run
```bash
python main.py
```

Next choose a option from the cli menu

