#-- https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/V



# Read N and M
N, M = map(int, input().split())

# Read array A
A = list(map(int, input().split()))

# Create frequency array of size M+1 (1-based indexing)
freq = [0] * (M + 1)

# Count frequencies
for x in A:
    freq[x] += 1

# Print results for 1 to M
for i in range(1, M + 1):
    print(freq[i])