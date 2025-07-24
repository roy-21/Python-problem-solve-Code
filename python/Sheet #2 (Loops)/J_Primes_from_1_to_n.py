# contest_link__ https://codeforces.com/group/MWSDmqGsZm/contest/219158


N = int(input())

for num in range(2, N + 1):  #2 to N number check
    is_prime = True  # Suppose the number is prime.
    for i in range(2, int(num**0.5) + 1):  # I will check up to the square root
        if num % i == 0:  # If the number is divisible by i
            is_prime = False  # is it not prime
            break  # loop close bcz it's not prime
    
    if is_prime:  # if is it prime, print it
        print(num, end=" ")  # space print




###another one 
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def print_primes(N):
#     for num in range(2, N + 1):
#         if is_prime(num):
#             print(num, end=" ")

# # Example Usage
# N = int(input())
# print_primes(N)
