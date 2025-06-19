# File Collector
![Platform: Windows](https://img.shields.io/badge/Platform-Windows-blue)

- Recursively collects files with specified extensions from multiple directories.

- Organizes matched files into subfolders named by extension within a single output folder.

## Usage
### 1. Clone the Repository
```bash
git clone https://github.com/lllDavid/file_collector
```
### 2. Run the Application

```bash
cd file_collector
python main.py
```
## Output Location
**By default, results are saved here**
```text
C:/Users/<your-username>/File_Collector/
```

**To change this, update the user_dir path in main.py:**
```text
user_dir = f"C:/Users/{user_name}/File_Collector"
```