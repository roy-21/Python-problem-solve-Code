# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/J


S = input().strip()

count = [0] * 26  # 26 letters

for ch in S:
    count[ord(ch) - ord('a')] += 1

for i in range(26):
    if count[i] > 0:
        print(f"{chr(i + ord('a'))} : {count[i]}")
        
