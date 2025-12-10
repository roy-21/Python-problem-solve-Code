# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/X


# Read N and M
N, M = map(int, input().split())

# Read grid
A = [input().strip() for _ in range(N)]

# Read X, Y (1-indexed)
X, Y = map(int, input().split())
X -= 1  # convert to 0-index
Y -= 1

# Directions for 8 neighbors
dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1), (1, 0), (1, 1)
]

ok = True

# Check each neighbor
for dx, dy in dirs:
    nx = X + dx
    ny = Y + dy

    # Check bounds
    if 0 <= nx < N and 0 <= ny < M:
        if A[nx][ny] != 'x':
            ok = False
            break

print("yes" if ok else "no")
