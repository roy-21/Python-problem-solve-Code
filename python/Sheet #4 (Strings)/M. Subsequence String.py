# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/M



s = input().strip()
target = "hello"
j = 0  # pointer for target

for ch in s:
    if ch == target[j]:
        j += 1
        if j == len(target):
            break

if j == len(target):
    print("YES")
else:
    print("NO")