N = int(input())
A = list(map(int, input().split()))

min_val = A[0]
freq = 0

for num in A:
    if num < min_val:
        min_val = num

for num in A:
    if num == min_val:
        freq += 1

if freq % 2 == 1:
    print("Lucky")
else:
    print("Unlucky")
