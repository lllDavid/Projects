# File Collector
![Platform: Windows](https://img.shields.io/badge/Platform-Windows-blue)
## Use Cases:
- Collect all files of a specific extension (e.g., .cfg, .sql, .json) from multiple directories into a single folder.

- Create a dedicated subfolder for each file extension within the main folder.

## Clone

```bash
git clone https://github.com/lllDavid/file_collector
```

## Save

To change the save location, adjust the path in user_dir variable (main.py):
```bash
user_dir = f"C:/Users/{user_name}/File_Collector"
```

## Start

```bash
cd file_collector
python main.py
```

## Usage

Choose directory to search in:
```bash
Enter directory to search in (e.g. C:/ ): 
```

Add pattern(s):
```bash
Enter search pattern(s), separated by commas (e.g. .json, .sql, .py):
```

Any matches are saved in the user_dir folder path.