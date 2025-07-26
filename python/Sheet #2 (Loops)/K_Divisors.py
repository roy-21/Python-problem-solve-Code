# contest_link__ https://codeforces.com/group/MWSDmqGsZm/contest/219158


def print_divisors(N):
    divisors = []
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:  
            divisors.append(i)  
            if i != N // i:  
                divisors.append(N // i)  
    
    divisors.sort()  # Ascending order e output dewa
    for d in divisors:
        print(d)

# Input neowa
N = int(input())
print_divisors(N)
