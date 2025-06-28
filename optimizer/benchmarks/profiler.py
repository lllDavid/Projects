from io import StringIO
from statistics import mean
from os import path, makedirs

from line_profiler import LineProfiler


profiling_results = []

# Saves profiling stats to a file and appends the result to a list.
def save_profiling_result(profile_type, func_name, stats_str):
    base_directory = 'benchmarks/results'
    directory = path.join(base_directory, profile_type)

    if not path.exists(directory):
        makedirs(directory)

    filename = path.join(directory, f"{func_name}.lprof")
    with open(filename, 'w') as f:
        f.write(stats_str)

    result_dict = {
        'profile_type': profile_type,
        'function_name': func_name,
        'stats': stats_str
    }
    profiling_results.append(result_dict)

    print(f"Finished profiling.")
    return result_dict

# Decorator to profile a function using LineProfiler and save the result.
def profile_function(profile_type="unoptimized"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            profiler = LineProfiler()
            profiler.add_function(func)
            result = profiler(func)(*args, **kwargs)

            stats_stream = StringIO()
            profiler.print_stats(stream=stats_stream)
            stats_str = stats_stream.getvalue()

            result_dict = save_profiling_result(profile_type, func.__name__, stats_str)
            
            return result, result_dict

        return wrapper
    return decorator

# Calculates mean profiling metrics per line across all saved profiling results.
def get_mean_profile_times():
    line_stats = {}
    line_contents = {}
    
    for result in profiling_results:
        stats_lines = result['stats'].split("\n")
        for line in stats_lines:
            parts = line.split()
            if len(parts) > 5 and parts[0].isdigit():  
                try:
                    line_num = int(parts[0])
                    hits = int(parts[1])       
                    time = float(parts[2])    
                    per_hit = float(parts[3])
                    percent_time = float(parts[4])  
                    line_content = " ".join(parts[5:])
                    
                    if line_num not in line_stats:
                        line_stats[line_num] = {'hits': [], 'time': [], 'per_hit': [], 'percent_time': []}
                        line_contents[line_num] = line_content
                    
                    line_stats[line_num]['hits'].append(hits)
                    line_stats[line_num]['time'].append(time)
                    line_stats[line_num]['per_hit'].append(per_hit)
                    line_stats[line_num]['percent_time'].append(percent_time)
                
                except ValueError:
                    pass  
    
    mean_results = {}
    for line_num, stats in line_stats.items():
        mean_results[line_num] = {
            "Mean Hits": mean(stats['hits']),
            "Mean Time": mean(stats['time']),
            "Mean Per Hit": mean(stats['per_hit']),
            "Mean % Time": mean(stats['percent_time'])
        }
    
    print("Mean Profiling Results Per Line:")
    print("Line #      Hits         Time  Per Hit   % Time  Line Contents")
    print("==========================================================================")
    for line_num, stats in sorted(mean_results.items()):
        print(f"{line_num:>5} {stats['Mean Hits']:>10.1f} {stats['Mean Time']:>10.1f} {stats['Mean Per Hit']:>10.1f} {stats['Mean % Time']:>10.1f}  {line_contents[line_num]}")
    
    return mean_results

def check_for_optimized_profiles():
    has_unoptimized = any(r['profile_type'] == 'unoptimized' for r in profiling_results)
    has_optimized = any(r['profile_type'] == 'optimized' for r in profiling_results)

    if has_unoptimized and not has_optimized:
        print("Warning: Only unoptimized profiling results found. Optimized results are missing.")
