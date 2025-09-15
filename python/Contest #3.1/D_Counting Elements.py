# https://codeforces.com/group/MWSDmqGsZm/contest/329103/problem/D


n = int(input())
a = list(map(int, input().split()))

count = 0
for x in a:
    if (x + 1) in a:
        count += 1
print(count)