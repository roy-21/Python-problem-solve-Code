T = int(input())

for _ in range(T):
    N = int(input())  
    A = list(map(int, input().split()))
    
    result = []  

    for i in range(N):
        current_max = A[i]
        for j in range(i, N):
            current_max = max(current_max, A[j])
            result.append(current_max)

    print(*result)
