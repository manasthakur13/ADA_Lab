from typing import List

def add_matrix(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """Helper to add two matrices."""
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def sub_matrix(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """Helper to subtract two matrices."""
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def strassen_recursive(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """Core recursive Strassen algorithm for 2^n x 2^n matrices."""
    n = len(A)
    
    # Base case: 1x1 matrix
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    mid = n // 2
    
    # Dividing the matrices into quadrants
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]
    
    # Calculating the 7 Strassen products (M1 to M7)
    M1 = strassen_recursive(add_matrix(A11, A22), add_matrix(B11, B22))
    M2 = strassen_recursive(add_matrix(A21, A22), B11)
    M3 = strassen_recursive(A11, sub_matrix(B12, B22))
    M4 = strassen_recursive(A22, sub_matrix(B21, B11))
    M5 = strassen_recursive(add_matrix(A11, A12), B22)
    M6 = strassen_recursive(sub_matrix(A21, A11), add_matrix(B11, B12))
    M7 = strassen_recursive(sub_matrix(A12, A22), add_matrix(B21, B22))
    
    # Combining the products into the result quadrants
    C11 = add_matrix(sub_matrix(add_matrix(M1, M4), M5), M7)
    C12 = add_matrix(M3, M5)
    C21 = add_matrix(M2, M4)
    C22 = add_matrix(add_matrix(sub_matrix(M1, M2), M3), M6)
    
    # Recombining quadrants into a single matrix
    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])
        
    return C

def next_power_of_two(n: int) -> int:
    """Finds the next power of 2 greater than or equal to n."""
    power = 1
    while power < n:
        power *= 2
    return power

def strassen_multiply(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """
    Strassen's Matrix Multiplication wrapper.
    Handles non-power-of-2 dimensions by padding with zeros.
    """
    # Get dimensions
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    if cols_A != rows_B:
        raise ValueError("Incompatible dimensions for multiplication.")
    
    # Find the dimension to pad to (maximum dimension of both matrices)
    max_dim = max(rows_A, cols_A, rows_B, cols_B)
    pad_size = next_power_of_two(max_dim)
    
    # Pad A and B with zeros
    A_padded = [[0] * pad_size for _ in range(pad_size)]
    B_padded = [[0] * pad_size for _ in range(pad_size)]
    
    for i in range(rows_A):
        for j in range(cols_A):
            A_padded[i][j] = A[i][j]
            
    for i in range(rows_B):
        for j in range(cols_B):
            B_padded[i][j] = B[i][j]
            
    # Compute using Strassen's algorithm
    C_padded = strassen_recursive(A_padded, B_padded)
    
    # Strip the padding to return the correct rows_A x cols_B result matrix
    C = []
    for i in range(rows_A):
        C.append(C_padded[i][:cols_B])
        
    return C

if __name__ == "__main__":
    # Test matrices (Can be non-square and not powers of 2)
    Matrix_A = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    
    Matrix_B = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]
    
    print("Matrix A:")
    for row in Matrix_A:
        print(row)
        
    print("\nMatrix B:")
    for row in Matrix_B:
        print(row)
        
    result = strassen_multiply(Matrix_A, Matrix_B)
    
    print("\nResult of Strassen Multiplication (A x B):")
    for row in result:
        print(row)