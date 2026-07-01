def shift_right(n, x, arr):
    # Reduce unnecessary full rotations
    x = x % n
    
    # Split and recombine using slicing
    # arr[-x:] gets the last x elements
    # arr[:-x] gets all elements except the last x
    if x > 0:
        shifted_arr = arr[-x:] + arr[:-x]
    else:
        shifted_arr = arr
        
    # Print elements separated by spaces
    print(*(shifted_arr))

def main():
    import sys
    # Read all inputs from standard input
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    n = int(data[0])
    x = int(data[1])
    arr = [int(i) for i in data[2:]]
    
    # Call the function to solve the problem
    shift_right(n, x, arr)

if __name__ == '__main__':
    main()
