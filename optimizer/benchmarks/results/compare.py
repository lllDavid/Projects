from os import path

def parse_lprof_text(lprof_text):
    parsed_data = {}

    lines = lprof_text.splitlines()

    data_start_index = None
    for idx, line in enumerate(lines):
        if line.strip().startswith("Line #"): 
            data_start_index = idx
            break

    if data_start_index is not None:
        for line in lines[data_start_index + 1:]:  
            columns = line.split()

            if len(columns) < 6 or columns[0].lower() == "line":
                continue

            try:
                line_num = int(columns[0])  
                hits = int(columns[1])  
                total_time = float(columns[2]) 
                per_hit_time = float(columns[3])  
                percent_time = float(columns[4]) 
                line_contents = " ".join(columns[5:])  

                parsed_data[line_num] = {
                    'hits': hits,
                    'time': total_time,
                    'per_hit_time': per_hit_time,
                    'percent_time': percent_time,
                    'line_contents': line_contents
                }
            except ValueError:
                continue

    return parsed_data

def load_lprof_file(file: str, directory: str):
    file_path = path.join(directory, file)
    if path.exists(file_path):
        with open(file_path, 'r') as f:
            lprof_text = f.read()

        stats_dict = parse_lprof_text(lprof_text)

        return stats_dict
    else:
        print(f"{directory.capitalize()} file '{file}' not found!")
        return None


def compare(file_name):
    unoptimized_stats = load_lprof_file(file_name, "benchmarks/results/unoptimized")
    optimized_stats = load_lprof_file(file_name, "benchmarks/results/optimized")

    if not unoptimized_stats or not optimized_stats:
        print("Error: One or both of the stats files are missing.")
        return

    total_unoptimized_time = 0
    total_optimized_time = 0

    all_line_nums = set(unoptimized_stats.keys()).union(optimized_stats.keys())

    for line_num in all_line_nums:
        unoptimized_data = unoptimized_stats.get(line_num)
        optimized_data = optimized_stats.get(line_num)

        if unoptimized_data and optimized_data:
            unoptimized_hits = unoptimized_data['hits']
            optimized_hits = optimized_data['hits']
            unoptimized_time = unoptimized_data['time']
            optimized_time = optimized_data['time']
            unoptimized_percent_time = unoptimized_data['percent_time']
            optimized_percent_time = optimized_data['percent_time']

            print(f"\nLine {line_num}: {unoptimized_data['line_contents']}")
            print(f"  Unoptimized Hits: {unoptimized_hits}, Optimized Hits: {optimized_hits}")
            print(f"  Unoptimized Total Time: {unoptimized_time:.6f}s, Optimized Total Time: {optimized_time:.6f}s")
            print(f"  Unoptimized % Time: {unoptimized_percent_time:.2f}%, Optimized % Time: {optimized_percent_time:.2f}%")
            time_change = optimized_time - unoptimized_time
            print(f"  Time Change: {time_change:.6f}s")

            total_unoptimized_time += unoptimized_time
            total_optimized_time += optimized_time
        else:
            if unoptimized_data:
                print(f"\nLine {line_num}: Present only in 'unoptimized' stats.")
            if optimized_data:
                print(f"\nLine {line_num}: Present only in 'optimized' stats.")

    if total_unoptimized_time > 0:
        performance_increase_percent = ((total_unoptimized_time - total_optimized_time) / total_unoptimized_time) * 100
        print(f"\nTotal Performance Increase: {performance_increase_percent:.2f}%")
    else:
        print("\nTotal performance increase: N/A (Unoptimized time is 0).")


