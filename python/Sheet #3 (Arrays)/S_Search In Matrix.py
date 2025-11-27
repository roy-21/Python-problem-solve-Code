# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/S

# Read N
N = int(input())

# Read arrays
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Sort both arrays
A.sort()
B.sort()

# Compare
if A == B:
    print("yes")
else:
    print("no")
