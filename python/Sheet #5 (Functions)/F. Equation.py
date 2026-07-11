import sys

def calculate_power(base, exponent):
    """
    Manually calculates base raised to the power of exponent (base^exponent).
    Does not use the built-in pow() or ** operator.
    """
    if exponent == 0:
        return 1
    
    result = 1
    for _ in range(exponent):
        result *= base
    return result

def solve_equation(x, n):
    """
    Calculates the sum S = (X^0 - 1) + X^2 + X^4 + ... up to the largest even power <= N.
    """
    total_sum = 0
    
    # Step through even powers from 0 up to N (inclusive)
    for power in range(0, n + 1, 2):
        term = calculate_power(x, power)
        
        # The first term (where power is 0) requires subtracting 1
        if power == 0:
            term -= 1
            
        total_sum += term
        
    return total_sum

def main():
    # Read inputs from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    x = int(input_data[0])
    n = int(input_data[1])
    
    # Calculate the result using the custom function
    ans = solve_equation(x, n)
    
    # Print the equation result
    print(ans)

if __name__ == '__main__':
    main()
