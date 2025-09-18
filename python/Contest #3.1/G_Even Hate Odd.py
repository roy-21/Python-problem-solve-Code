# https://codeforces.com/group/MWSDmqGsZm/contest/329103/problem/G

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if n % 2 != 0:
        print(-1)
    else:
        even_count = sum(1 for num in arr if num % 2 == 0)
        print(abs(even_count - n // 2))