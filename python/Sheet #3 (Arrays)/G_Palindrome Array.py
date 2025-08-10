N = int(input())
A = list(map(int, input().split()))

is_palindrome = True

for i in range(N // 2):
    if A[i] != A[N - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("YES")
else:
    print("NO")