# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/I


S = input().strip()

if S == S[::-1]:
    print("YES")
else:
    print("NO")