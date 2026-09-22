import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    result = []
    N = len(A)
    M = len(A[0])
    
    for j in range(M):
        new_row = []
        for i in range(N):
            new_row.append(A[i][j])
        result.append(new_row)
    return np.asarray(result)
    pass
