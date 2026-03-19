# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/L

N, Q = map(int, input().split())
S = list(input().strip())

for _ in range(Q):
    query = input().split()
    
    if query[0] == "pop_back":
        S.pop()
    
    elif query[0] == "front":
        print(S[0])
    
    elif query[0] == "back":
        print(S[-1])
    
    elif query[0] == "sort":
        l = int(query[1]) - 1
        r = int(query[2]) - 1
        S[l:r+1] = sorted(S[l:r+1])
    
    elif query[0] == "reverse":
        l = int(query[1]) - 1
        r = int(query[2]) - 1
        S[l:r+1] = S[l:r+1][::-1]
    
    elif query[0] == "print":
        pos = int(query[1]) - 1
        print(S[pos])
    
    elif query[0] == "substr":
        l = int(query[1]) - 1
        r = int(query[2]) - 1
        print("".join(S[l:r+1]))
    
    elif query[0] == "push_back":
        S.append(query[1])