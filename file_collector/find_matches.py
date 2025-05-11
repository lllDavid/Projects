from os import path as p, walk, listdir
from concurrent.futures import ThreadPoolExecutor

def is_excluded(path, exclude_dirs):
    norm_path = p.normcase(p.normpath(path))
    return any(norm_path.startswith(ex) for ex in exclude_dirs)

def process_directory(current_dir, ext_set, exclude_dirs):
    found = []
    for root, _, files in walk(current_dir):
        if is_excluded(root, exclude_dirs):
            continue
        for f in files:
            if p.splitext(f)[1].lower() in ext_set:
                found.append(p.join(root, f))
    return found

def find_matches(search_dir, file_extensions, exclude_dirs=None):
    ext_set = {ext.lower() for ext in file_extensions}
    exclude_dirs = [p.normcase(p.normpath(d)) for d in (exclude_dirs or [])]

    print("Starting search in provided directory...")

    top_dirs = [
        p.join(search_dir, d) for d in listdir(search_dir)
        if p.isdir(p.join(search_dir, d)) and not is_excluded(p.join(search_dir, d), exclude_dirs)
    ]

    found_paths = []
    
    with ThreadPoolExecutor(max_workers=8) as pool:
        for sublist in pool.map(lambda d: process_directory(d, ext_set, exclude_dirs), top_dirs):
            found_paths.extend(sublist)

    print(f"Search completed. Found {len(found_paths)} matching files.")
    return found_paths
