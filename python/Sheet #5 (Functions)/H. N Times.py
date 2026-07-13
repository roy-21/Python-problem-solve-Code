import sys

def print_character_n_times(n, c):
    """
    Prints the character C, N times, separated by a space.
    """
    # Create a list of the character repeated N times, then join with spaces
    result = " ".join([c] * n)
    print(result)

def main():
    # Read all inputs from standard input efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # First element is the number of test cases T
    t = int(input_data[0])
    
    index = 1
    for _ in range(t):
        # Read N and character C for each test case
        n = int(input_data[index])
        c = input_data[index + 1]
        
        # Call the function to handle printing
        print_character_n_times(n, c)
        
        # Move to the next testcase pair
        index += 2

if __name__ == '__main__':
    main()
