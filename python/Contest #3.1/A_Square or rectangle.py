#problem:- https://codeforces.com/group/MWSDmqGsZm/contest/329103/problem/A

# Number of test cases
t = int(input())

for _ in range(t):
    w, h = map(int, input().split())
    
    if w == h:
        print("Square")
    else:
        print("Rectangle")