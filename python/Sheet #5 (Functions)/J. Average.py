import sys

def calculate_average(numbers_list):
    """
    Calculates the mean of a list of numbers.
    """
    if not numbers_list:
        return 0.0
    return sum(numbers_list) / len(numbers_list)

def main():
    # Read all inputs from standard input efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # First element is the size N
    n = int(input_data[0])
    
    # The remaining elements are the array values
    # Convert them to floats to handle decimal inputs accurately
    numbers = [float(x) for x in input_data[1:n+1]]
    
    # Call the function to find the mean
    average = calculate_average(numbers)
    
    # Print the result formatted strictly to 6 decimal places
    print(f"{average:.6f}")

if __name__ == '__main__':
    main()
