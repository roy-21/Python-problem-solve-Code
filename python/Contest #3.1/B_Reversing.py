# https://codeforces.com/group/MWSDmqGsZm/contest/329103/problem/B


n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    if a[i] == 0:
        a[:i] = reversed(a[:i])   
print(*a)