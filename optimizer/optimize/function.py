# This method is inefficient because it uses three nested loops, resulting in a time complexity of O(n^3).
def matrix_multiplication(A, B):
    n = len(A)  
    C = [[0] * n for _ in range(n)]  
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C