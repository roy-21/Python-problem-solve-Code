#Input
N = int(input())
A = list(map(int, input().split()))

#Initialize operation count
operations = 0

#Keep performing the operation while all numbers are even
while all(a % 2 == 0 for a in A):
    A = [a // 2 for a in A]  # Divide all numbers by 2
    operations += 1

print(operations)