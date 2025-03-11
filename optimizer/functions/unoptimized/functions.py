# Unoptimized functions
from benchmarks.profiler import profile_function
from benchmarks.time import time_function

# 1
@time_function(repetitions=10)
@profile_function(profile_type="unoptimized")
def inefficient_duplicates_check(data):
    """
    This function is inefficient because it checks for duplicates by comparing
    every element to every other element using nested loops.
    """
    duplicates = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j] and data[i] not in duplicates:
                duplicates.append(data[i])
    return duplicates

# 2
@time_function(repetitions=10)
@profile_function(profile_type="unoptimized")
def inefficient_matrix_multiplication(A, B):
    """
    Perform matrix multiplication using nested loops.
    This method is inefficient because it uses three nested loops, resulting in a time complexity of O(n^3).
    """
    n = len(A)  
    C = [[0] * n for _ in range(n)]  
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

# 3
@time_function(repetitions=10)
@profile_function(profile_type="unoptimized")
def inefficient_sorting_repeatedly(n):
    """
    Generate a list of `n` random numbers and sort it repeatedly.
    This function uses bubble sort for sorting, which is inefficient.
    """
    import random

    def bubble_sort(arr):
        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    numbers = [random.randint(1, 1000) for _ in range(n)]
    
    for _ in range(100):  
        bubble_sort(numbers)
    
    return numbers

