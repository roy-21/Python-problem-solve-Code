def is_odd(n):
    """Checks if the given number is odd."""
    return n % 2 != 0

def is_binary_palindrome(n):
    """Checks if the binary representation of the number is a palindrome."""
    # bin(n) returns a string like '0b11', so we slice from index 2 to remove '0b'
    binary_str = bin(n)[2:]
    return binary_str == binary_str[::-1]

def main():
    # Read the input number
    n = int(input())
    
    # Check both conditions using the two functions
    if is_odd(n) and is_binary_palindrome(n):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
