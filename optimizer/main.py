import time
import threading
from functions.unoptimized.functions import main as unoptimized
from benchmarks.results.analyze import analyze
from benchmarks.results.compare import compare
from benchmarks.profiler import get_mean_profile_times
from optimize.optimize_cython import main as opt_main

optimized = None  
# Delay import until content of functions/optimized/test_func is generated after running Option 0. 
def try_import_optimized():
    global optimized
    while optimized is None:
        try:
            from functions.optimized.test_func.run import main as optimized
            print("\n Successfully imported optimized function!")
            break 
        except ImportError:
            print("\n Optimized function not yet in dir. Retrying in 15 seconds...")
            time.sleep(15)  

threading.Thread(target=try_import_optimized, daemon=True).start()

def menu():
    print("\n--- Menu ---")
    # 0. see /optimize ; this optimizes a .py func using cython 
    print("0. Optimize a function (Function currently hardcoded)")
    # 1. profiles functions and shows before vs. after execution times / change repetitions time in /functions/unoptimized on @time_function 
    print("1. Compare unoptimized vs. optimized functions")
    # 2. eg. analyze inefficient_matrix_multiplication.lprof after running Option 1
    print("2. Analyze a function by execution time")
    # 3. TODO: currently prints same values for unoptimized and optimized (should be unoptimized then optimized) + only works after running Option 1
    print("3. Print profiling stats for file")
    # 4. TODO: currently only works if files with same name in benchmarks/results/optimized and benchmarks/results/unoptimized
    print("4. Compare profile times")
    print("5. Exit")

def optimize_function():
    opt_main()

def compare_functions():
    print(f"\n--- Running Unoptimized version of matrix multiplication ---\n")
    unoptimized()

    if optimized:
        print("\n--- Running Optimized version of matrix multiplication ---\n")
        optimized()
    else:
        print("\nOptimized function is still being imported. Please try again later.")

def analyze_by_execution_time():
    print("\n--- Analyzing by execution time ---")
    analyze()  

def print_profiling_stats():
    print("\n--- Profiling results of unoptimized: ---")
    get_mean_profile_times()

    print("\n--- Profiling results of optimized: ---")
    if optimized:
        get_mean_profile_times()
    else:
        print("\nOptimized function is still being imported. Please try again later.")

def compare_files():
    file_name = input("\nEnter the filename to compare: \n").strip()
    print(f"\n--- Comparing results using file: {file_name} ---\n")
    compare(file_name)

def main():
    while True:
        menu()  
        choice = input("Choose an option (0-5): ").strip()

        if choice == "0":
            optimize_function()
        elif choice == '1':
            compare_functions()
        elif choice == '2':
            analyze_by_execution_time()
        elif choice == '3':
            print_profiling_stats()
        elif choice == '4':
            compare_files()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
