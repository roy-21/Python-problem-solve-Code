#https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/R



n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if sorted(A) == sorted(B):
    print("yes")
else:
    print("no")
