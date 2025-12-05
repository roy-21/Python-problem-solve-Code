# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/W

# Read N and M
N, M = map(int, input().split())

# Process each row
for _ in range(N):
    row = list(map(int, input().split()))
    reversed_row = row[::-1]   # reverse the row
    print(*reversed_row)