from os import path as p, makedirs
from shutil import copy

def copy_matches(user_dir, found_paths):
    for path in found_paths:
        dest_path = p.join(user_dir)

        if p.isfile(path):
            makedirs(p.dirname(dest_path), exist_ok=True)
            copy(path, dest_path)

        