from time import sleep
from inspect import unwrap
from threading import Thread

from benchmarks.analyze import analyze
from benchmarks.profiler import get_mean_profile_times, get_performance_gain

from optimize.optimizer import main as optimizer
from functions.unoptimized.matrix_multiplication import main as unoptimized


optimized= None  

def try_import():
    global optimized
    first_try = True  
    
    while optimized is None:
        try:
            # TODO: Remove hardcoded path
            from functions.optimized.matrix_multiplication.run import main as optimized
            print("\nSuccessfully imported optimized function!")
            break
        except ImportError:
            if first_try:
                print("\nNo optimized function in directory. Retrying in 5 seconds.")
                first_try = False
                sleep(5)

Thread(target=try_import, daemon=True).start()

def options():
    print("\n1. Convert function to Cython")

    print("2. Benchmark unoptimized vs. optimized function (Run after Option 1)") 

    print("3. Rank bottlenecks in unoptimzed function by execution time (Run after Option 1)") 

    print("4. Print profiling stats for file (Run after Option 2)") # NOTE: Doesnt work correctly

    print("5. Exit")

def optimize_function():
    optimizer()

def benchmark_functions():
    if optimized is None:
        print("\nOptimized function is still being imported. Please try again later.")
        return

    module_name = unwrap(optimized).__module__.split('.')[-2]

    for func, label in ((unoptimized, "Unoptimized"), (optimized, "Optimized")):
        print(f"\nRunning {label} version of {module_name}:")
        func()
        if label == "Optimized":
            get_performance_gain(f"{module_name}.lprof")

def rank_by_execution_time():
    print("\nAnalyzing by execution time:")
    analyze()  

def print_profiling_stats():
    print("\nProfiling results of unoptimized:")
    get_mean_profile_times()

    print("\nProfiling results of optimized:")
    if optimized:
        get_mean_profile_times()
    else:
        print("\nOptimized function is still being imported. Please try again later.")

def main():
    while True:
        options()
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            optimize_function()
        elif choice == '2':
            benchmark_functions()
        elif choice == '3':
            rank_by_execution_time()
        elif choice == '4':
            print_profiling_stats()
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid option. Please try again.")
            continue

        x = input("\nContinue? (y/n): ").strip().lower()
        if x != 'y':
            print("Exiting.")
            break

main()