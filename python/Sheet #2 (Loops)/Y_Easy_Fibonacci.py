# contest_link__ https://codeforces.com/group/MWSDmqGsZm/contest/219158


N = int(input())

a, b = 0, 1
for _ in range(N):
    print(a, end=' ')
    a, b = b, a + b
