from os import path, getlogin, makedirs

from find_matches import find_matches
from copy_matches import copy_matches

def main():
    search_dir = input("Enter directory to search in (e.g. C:/ ): ").strip()

    raw = input("Enter search pattern(s), separated by commas (e.g. .json, .sql, .py): ")
    patterns = [p.strip() for p in raw.split(',') if p.strip()]

    user = getlogin()
    base_out = path.join("C:/Users", user, "File_Collector")
    makedirs(base_out, exist_ok=True)

    recycle_bin = path.join(search_dir, "$Recycle.Bin")
    exclude = [recycle_bin, base_out]

    for pat in patterns:
        folder = pat.lstrip(".").lower() or "misc"
        out_dir = path.join(base_out, folder)
        makedirs(out_dir, exist_ok=True)

        print(f"\nSearching for *{pat}* files...")
        matches = find_matches(search_dir, [pat], exclude_dirs=exclude)

        if matches:
            print(f"Found {len(matches)} files. Copying...")
            copy_matches(out_dir, matches)
        else:
            print(f"No *{pat}* files found.")

if __name__ == "__main__":
    main()