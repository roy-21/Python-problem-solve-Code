# contest_link__ https://codeforces.com/group/MWSDmqGsZm/contest/219158


N, A, B = map(int,input().split())

total_sum = 0

for i in range(1, N+1):
    digit_sum = sum(int(digit) for digit in str(i))
    if A <= digit_sum <= B:
        total_sum += i

print(total_sum)