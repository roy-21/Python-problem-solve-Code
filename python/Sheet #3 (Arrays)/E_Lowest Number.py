N = int(input())
A = list(map(int, input().split()))

min_value = A[0]
min_index = 0

for i in range(1, N):
    if A[i] < min_value:
        min_value = A[i]
        min_index = i
        
print(min_value, min_index + 1)

