# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/K


N = int(input().strip())

for _ in range(N):
    S, T = input().split()
    
    result = []
    min_len = min(len(S), len(T))
    
    # Alternate characters
    for i in range(min_len):
        result.append(S[i])
        result.append(T[i])
    
    # Add remaining part
    result.append(S[min_len:])
    result.append(T[min_len:])
    
    print("".join(result))