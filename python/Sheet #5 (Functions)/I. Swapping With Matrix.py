import sys

def swap_matrix_elements(matrix, n, x, y):
    # Convert 1-based indexing to 0-based indexing
    idx_x = x - 1
    idx_y = y - 1
    
    # 1. Swap Row X and Row Y
    matrix[idx_x], matrix[idx_y] = matrix[idx_y], matrix[idx_x]
    
    # 2. Swap Column X and Column Y
    for r in range(n):
        matrix[r][idx_x], matrix[r][idx_y] = matrix[r][idx_y], matrix[r][idx_x]
        
    # Print the resulting matrix
    for row in matrix:
        print(*(row))

def main():
    # Fast I/O for competitive programming
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])
    x = int(input_data[1])
    y = int(input_data[2])
    
    # Reconstruct the N x N matrix from flat data
    matrix = []
    idx = 3
    for _ in range(n):
        row = [int(val) for val in input_data[idx : idx + n]]
        matrix.append(row)
        idx += n
        
    # Execute matrix operations using the function
    swap_matrix_elements(matrix, n, x, y)

if __name__ == "__main__":
    main()
