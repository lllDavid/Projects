from os import path
import re

def get_total_time(lprof_text):
    match = re.search(r"Total time:\s*([\d\.]+)\s*s", lprof_text)
    if match:
        return float(match.group(1))
    return None

def load_total_time(file: str, directory: str):
    file_path = path.join(directory, file)
    if path.exists(file_path):
        with open(file_path, 'r') as f:
            lprof_text = f.read()
        return get_total_time(lprof_text)
    else:
        print(f"{directory.capitalize()} file '{file}' not found!")
        return None

def compare(file_name):
    total_unoptimized_time = load_total_time(file_name, "benchmarks/results/unoptimized")
    total_optimized_time = load_total_time(file_name, "benchmarks/results/optimized")

    if total_unoptimized_time is None or total_optimized_time is None:
        print("Error: One or both of the stats files are missing or malformed.")
        return

    if total_unoptimized_time > 0:
        percent_faster = ((total_unoptimized_time - total_optimized_time) / total_unoptimized_time) * 100
        print(f"Performance increase: {percent_faster:.2f}%")
    else:
        print("N/A")
