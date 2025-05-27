# Use this func to let optimize_cython.py optimize it
def test_func(A, B):
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


