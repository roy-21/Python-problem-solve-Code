import sys

def find_min_and_max(numbers):
    """
    Finds and returns the minimum and maximum values from a list.
    """
    minimum_value = min(numbers)
    maximum_value = max(numbers)
    return minimum_value, maximum_value

def main():
    # Read all inputs from standard input efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # First element is the size N
    n = int(input_data[0])
    
    # The remaining N elements are the array values
    numbers = [int(x) for x in input_data[1:n+1]]
    
    # Call the function to find the min and max
    min_val, max_val = find_min_and_max(numbers)
    
    # Print the minimum and maximum separated by a space
    print(f"{min_val} {max_val}")

if __name__ == '__main__':
    main()
