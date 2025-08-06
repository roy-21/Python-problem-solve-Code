'''
https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/B
'''

N = int(input())                      
A = list(map(int, input().split()))  
X = int(input())                     

found = False
for i in range(N):
    if A[i] == X:
        print(i)    
        found = True
        break       

if not found:
    print(-1)
