from shutil import copy2
from os import path as p, makedirs
from concurrent.futures import ThreadPoolExecutor

def copy_file_with_unique_name(src_path, dest_dir, existing_files, failed_files, copy_count):
    filename = p.basename(src_path)
    dest_path = p.join(dest_dir, filename)

    if dest_path in existing_files:
        name, ext = p.splitext(filename)
        counter = 1
        while True:
            new_filename = f"{name}_{counter}{ext}"
            dest_path = p.join(dest_dir, new_filename)
            if dest_path not in existing_files:
                break
            counter += 1

    existing_files.add(dest_path)

    try:
        if p.isfile(src_path):
            copy2(src_path, dest_path)
            copy_count[0] += 1  
    except Exception as e:
        failed_files.append((src_path, str(e)))

def copy_matches(user_dir, found_paths):
    makedirs(user_dir, exist_ok=True)

    existing_files = set(p.join(user_dir, p.basename(fp)) for fp in found_paths)
    failed_files = [] 
    copy_count = [0] 

    with ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(lambda fp: copy_file_with_unique_name(fp, user_dir, existing_files, failed_files, copy_count), found_paths)

    print(f"Successfully copied {copy_count[0]} files to {user_dir}")
    
    if failed_files:
        print("\nThe following files couldn't be copied:")
        for src, error in failed_files:
            print(f"File: {src} | Error: {error}")