## Use Cases:

- Combine **all** files with a specific file **extension** into **one** folder (e.g ".yml", ".jpg", ".json" ...)

- Combine files from **different locations** into **one** folder (e.g. file1.txt in one folder, file2.md in other folder...)

## Clone

```bash
git clone https://github.com/lllDavid/file_collector
```

## Save

To change the **save** location, adjust the path in **user_dir** variable (main.py):
```bash
user_dir = f"C:/Users/{user_name}/File_Collector"
```

## Start

```bash
cd file_collector
python main.py
```

## Usage

Choose **directory** to search in:
```bash
Enter directory to search in (eg. C:/ ): 
```

Add **pattern/s** (eg. .yml or file1.txt then file2.txt...) next type **s** to perform search:
```bash
Add a search pattern (or type 's' to search):
```

Any matches are **saved** in the user_dir folder path.