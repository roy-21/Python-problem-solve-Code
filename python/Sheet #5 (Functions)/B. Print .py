def print_numbers(n: int):
    # Loop from 1 to N
    for i in range(1, n + 1):
        if i == n:
            print(i, end="")  # No trailing space for the last number
        else:
            print(i, end=" ") # Space separated for other numbers

if __name__ == "__main__":
    # Read the integer input
    n = int(input())
    # Call the function
    print_numbers(n)
