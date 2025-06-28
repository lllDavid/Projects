from time import sleep
from threading import Thread

from benchmarks.results.analyze import analyze
from benchmarks.results.compare import compare
from benchmarks.profiler import get_mean_profile_times

from optimize.optimize_cython import main as optim_main
from functions.unoptimized.functions import main as unoptim_main


imported= None  
def try_import_optimized():
    global imported
    first_try = True  
    
    while imported is None:
        try:
            from functions.optimized.matrix_multiplication.run import main as imported
            print("\nSuccessfully imported optimized function!")
            break
        except ImportError:
            if first_try:
                print("\nOptimized function not yet in dir. Retrying in 5 seconds.")
                first_try = False
                sleep(5)

Thread(target=try_import_optimized, daemon=True).start()

def options():
    print("\n1. Convert function to Cython")

    print("2. Benchmark: Unoptimized vs. Optimized function") # Use after converting a function

    print("3. Rank bottlenecks in a unoptimzed function by execution time") #  Use after converting a function

    print("4. Print profiling stats for file") # NOTE: Doesnt work correctly

    print("5. See total perfromance increase") #  Use after converting a function

    print("6. Exit")

def optimize_function():
    optim_main()

def compare_functions():
    print(f"\n--- Running Unoptimized version of matrix multiplication ---")
    unoptim_main()

    if imported:
        print("\n--- Running Optimized version of matrix multiplication ---")
        imported()
    else:
        print("\nOptimized function is still being imported. Please try again later.")

def analyze_by_execution_time():
    print("\n--- Analyzing by execution time ---")
    analyze()  

def print_profiling_stats():
    print("\n--- Profiling results of unoptimized: ---")
    get_mean_profile_times()

    print("\n--- Profiling results of optimized: ---")
    if imported:
        get_mean_profile_times()
    else:
        print("\nOptimized function is still being imported. Please try again later.")

def compare_files():
    file_name = input("\nEnter the filename to compare (e.g. matrix_multiplication.lprof): \n").strip()
    print(f"\n--- Comparing results using file: {file_name} ---\n")
    compare(file_name)

def main():
    while True:
        options()  
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            optimize_function()
        elif choice == '2':
            compare_functions()
        elif choice == '3':
            analyze_by_execution_time()
        elif choice == '4':
            print_profiling_stats()
        elif choice == '5':
            compare_files()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

main()