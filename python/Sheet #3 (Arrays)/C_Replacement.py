'''
# problem_link__ https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/C
'''

N = int(input())
arr = list(map(int, input().split()))

for i in range(N):
    if arr[i] > 0:
        arr[i] = 1
    elif arr[i] < 0:
        arr[i] = 2

print(*arr)
