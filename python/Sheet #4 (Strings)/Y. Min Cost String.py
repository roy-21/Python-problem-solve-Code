#https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/Y

import sys
input = sys.stdin.readline

# Input
s = list(input().strip())
cost = list(map(int, input().split()))

n = len(s)

def get_cost(a, b):
    return abs(cost[ord(a) - ord('a')] - cost[ord(b) - ord('a')])

# Replace '?'
for i in range(n):
    if s[i] == '?':
        best_char = 'a'
        best_val = float('inf')

        for c in range(26):
            ch = chr(ord('a') + c)
            val = 0

            # left neighbor
            if i > 0:
                val += get_cost(s[i - 1], ch)

            # right neighbor (only if not '?')
            if i < n - 1 and s[i + 1] != '?':
                val += get_cost(ch, s[i + 1])

            if val < best_val or (val == best_val and ch < best_char):
                best_val = val
                best_char = ch

        s[i] = best_char

# Calculate total cost
total_cost = 0
for i in range(1, n):
    total_cost += get_cost(s[i - 1], s[i])

# Output
print(total_cost)
print("".join(s))