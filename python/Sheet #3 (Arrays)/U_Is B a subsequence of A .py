#-- https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/U



# Read N and M
N, M = map(int, input().split())

# Read arrays
A = list(map(int, input().split()))
B = list(map(int, input().split()))

i = 0  # pointer for A
j = 0  # pointer for B

# Traverse A and try matching elements of B
while i < N and j < M:
    if A[i] == B[j]:
        j += 1   # if matched, move pointer of B
    i += 1       # always move pointer of A

# If j reached M, all elements of B found in order
if j == M:
    print("YES")
else:
    print("NO")
