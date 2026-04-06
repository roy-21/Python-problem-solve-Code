# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/N


n = int(input())
s = input().strip()

max_sub_len = 0
last_char = ''

for ch in s:
    if ch != last_char:
        max_sub_len += 1
        last_char = ch

print(max_sub_len)