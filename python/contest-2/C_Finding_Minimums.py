n, k = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(0, n, k):
    group = arr[i:i+k]  
    print(min(group), end=' ')
