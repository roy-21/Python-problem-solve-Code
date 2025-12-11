# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/Y


# Read N and Q
N, Q = map(int, input().split())

# Read array A
A = list(map(int, input().split()))

# Build prefix sum (1-indexed)
prefix = [0] * (N + 1)

for i in range(1, N + 1):
    prefix[i] = prefix[i-1] + A[i-1]

# Answer each query
for _ in range(Q):
    L, R = map(int, input().split())
    print(prefix[R] - prefix[L-1])
