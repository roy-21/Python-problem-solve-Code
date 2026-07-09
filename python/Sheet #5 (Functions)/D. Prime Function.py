import sys
import math

def is_prime(n):
    """
    Checks if a number N is prime in O(sqrt(N)) time complexity.
    """
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    
    # 2 is the only even prime number
    if n == 2:
        return True
    
    # Exclude all other even numbers
    if n % 2 == 0:
        return False
    
    # Check odd factors up to the square root of N
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
            
    return True

def main():
    # Read all inputs efficiently from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # First element is the number of test cases T
    t = int(input_data[0])
    
    # Output list to store answers for all test cases
    results = []
    
    for i in range(1, t + 1):
        n = int(input_data[i])
        
        # Check if the number is prime using the function
        if is_prime(n):
            results.append("YES")
        else:
            results.append("NO")
            
    # Print all results separated by newlines
    print("\n".join(results))

if __name__ == '__main__':
    main()
