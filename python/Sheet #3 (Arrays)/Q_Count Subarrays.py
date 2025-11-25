#https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/Q


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    count = 0
    length = 1  # every element starts a segment
    
    for i in range(1, n):
        if arr[i] >= arr[i-1]:
            length += 1
        else:
            count += length * (length + 1) // 2
            length = 1
    
    count += length * (length + 1) // 2
    
    print(count)
