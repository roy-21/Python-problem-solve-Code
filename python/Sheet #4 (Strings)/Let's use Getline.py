# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/B



s = input()

for ch in s:
    if ch == '\\':
        break
    print(ch, end='')