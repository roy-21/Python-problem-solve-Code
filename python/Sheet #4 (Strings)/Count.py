# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/E


# Input
S = input().strip()

# Sum of digits
total = 0
for ch in S:
    total += int(ch)

print(total)


# olternative solution using list comprehension and sum function:

# S = input().strip()
# print(sum(ord(ch) - ord('0') for ch in S))