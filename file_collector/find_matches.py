from os import path, walk

def find_matches(search_dir, search_patterns):
    found_paths = []
    for current_dir, sub_dirs, files in walk(search_dir):
        for file in files:
            for pattern in search_patterns:
                if pattern.lower() in file.lower():  
                    found_paths.append(path.join(current_dir, file))

        for sub_dir in sub_dirs:
            for pattern in search_patterns:
                if pattern.lower() in sub_dir.lower(): 
                    found_paths.append(path.join(current_dir, sub_dir))
    
    return found_paths
