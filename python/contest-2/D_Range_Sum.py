contest-link:- https://codeforces.com/group/MWSDmqGsZm/contest/326907


T = int(input())

for _ in range(T):
    L, R = map(int, input().split())
    Total = R*(R+1)//2 - L*(L-1)//2
    print(Total)
