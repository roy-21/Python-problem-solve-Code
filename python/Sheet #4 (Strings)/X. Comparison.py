#https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/X


s = input().strip()
n = len(s)

# If cannot split
if n == 1:
    print(s)
else:
    best = None

    for i in range(1, n):
        left = ''.join(sorted(s[:i]))
        right = ''.join(sorted(s[i:]))
        candidate = left + right

        if best is None or candidate < best:
            best = candidate

    print(best)