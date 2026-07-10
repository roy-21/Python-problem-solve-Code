import sys

def swap_numbers(x, y):
    """
    Swaps two numbers and returns them in reversed order.
    """
    # Python allows direct packing and unpacking to swap variables
    x, y = y, x
    return x, y

def main():
    # Read inputs from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    x = int(input_data[0])
    y = int(input_data[1])
    
    # Call the function to swap the values
    swapped_x, swapped_y = swap_numbers(x, y)
    
    # Print the swapped results separated by a space
    print(f"{swapped_x} {swapped_y}")

if __name__ == '__main__':
    main()
