def create_new_array(arr_a, arr_b):
    # Concatenate array B followed by array A
    return arr_b + arr_a

def main():
    # Read the size of the arrays (not strictly needed for Python list operations, but part of input)
    n = int(input())
    
    # Read array A and array B elements
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    
    # Get the concatenated array using the function
    arr_c = create_new_array(arr_a, arr_b)
    
    # Print the elements separated by space
    print(*(arr_c))

if __name__ == "__main__":
    main()
