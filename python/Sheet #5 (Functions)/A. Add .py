def calculate_sum(x: int, y: int) -> int:
    """Returns the summation of two numbers."""
    return x + y

def main():
    # Read a single line, split by spaces, and convert to integers
    x, y = map(int, input().split())
    
    # Call the function and print the result
    print(calculate_sum(x, y))

if __name__ == "__main__":
    main()
