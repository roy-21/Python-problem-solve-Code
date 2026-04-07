# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/O


import sys
input = sys.stdin.readline

# Input
N = int(input())
S = input().strip()

# Count array for 26 lowercase letters
count = [0] * 26

# Count letters
for ch in S:
    count[ord(ch) - ord('a')] += 1

# Reconstruct sorted string
res = []
for i in range(26):
    res.append(chr(ord('a') + i) * count[i])

print(''.join(res))