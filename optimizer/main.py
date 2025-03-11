from random import randint
from functions.unoptimized.functions import inefficient_matrix_multiplication as unoptimized
from functions.optimized.functions import inefficient_matrix_multiplication as optimized
from benchmarks.results.analyze import analyze
from benchmarks.results.compare import compare
from benchmarks.profiler import get_mean_profile_times

def run_matrix_multiplication(matrix_a, matrix_b, method_name):
    print(f"\n--- Running '{method_name}' version of matrix multiplication ---\n")
    
    if method_name == 'unoptimized':
        unoptimized(matrix_a, matrix_b)
    elif method_name == 'optimized':
        optimized(matrix_a, matrix_b)
    else:
        print("Unknown method name")
        return
    
    print("\n--- Profiling results: ---\n")
    get_mean_profile_times()
    print("\n--- Analysis: ---\n")
    analyze()

def main():
    size = 50
    min_val = 1
    max_val = 10

    matrix_a = [[randint(min_val, max_val) for _ in range(size)] for _ in range(size)]
    matrix_b = [[randint(min_val, max_val) for _ in range(size)] for _ in range(size)]

    method = input("Choose method ('unoptimized' or 'optimized'): ").strip().lower()
    if method not in ['unoptimized', 'optimized']:
        print("Invalid choice. Please run the program again.")
        return

    run_matrix_multiplication(matrix_a, matrix_b, method)

    file_name = input("\nEnter the filename to compare: \n").strip()
    print(f"\n--- Comparing results using file: {file_name} --- \n")
    compare(file_name)

if __name__ == "__main__":
    main()
