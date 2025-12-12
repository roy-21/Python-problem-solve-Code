# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/Z


# Read N and Q
N, Q = map(int, input().split())

# Read array A
A = list(map(int, input().split()))

# Sort the array for binary search
A.sort()

# Binary search function
def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Process each query
for _ in range(Q):
    X = int(input())
    print("found" if binary_search(A, X) else "not found")