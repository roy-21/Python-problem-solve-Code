# contest_link__ https://codeforces.com/group/MWSDmqGsZm/contest/219158


import math

def is_prime(X):
    if X < 2:
        print("NO")
    for i in range(2, int(math.sqrt(X)) + 1):
        if X % i == 0:
            return "NO"
    return "YES"

X = int(input().strip())

print(is_prime(X))