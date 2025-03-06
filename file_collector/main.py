from os import path, getlogin, makedirs

from find_matches import find_matches
from copy_matches import copy_matches

def main():
    search_dir = str(input("Enter directory to search in (e.g., C:/ ): "))
    search_patterns = []

    while True:
        user_input = input("Add a search pattern (or type 's' to search): ")

        if user_input.lower() == 's':
            break

        search_patterns.append(user_input)

    user_name = getlogin()
    user_dir = f"C:/Users/{user_name}/File_Collector"

    if not path.exists(user_dir):
        makedirs(user_dir)

    print(f"Searching for files and folders in {search_dir}...")

    found_paths = find_matches(search_dir, search_patterns)

    if found_paths:
        print(f"Found {len(found_paths)} matching files/folders. Copying them...")
        copy_matches(user_dir, found_paths)
        print(f"Files copied successfully to {user_dir}.")
    else:
        print("No matching files found.")

if __name__ == "__main__":
    main()
