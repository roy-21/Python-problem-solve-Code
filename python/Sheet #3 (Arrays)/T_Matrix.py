#https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/T


# Read N
N = int(input())

primary_sum = 0
secondary_sum = 0

# Read matrix row by row
for i in range(N):
    row = list(map(int, input().split()))

    primary_sum += row[i]          # Primary diagonal
    secondary_sum += row[N - 1 - i]  # Secondary diagonal

# Print absolute difference
print(abs(primary_sum - secondary_sum))
