# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/P

import re

s = input().strip()

# Replace everything except letters with space
s_clean = re.sub(r'[^a-zA-Z]', ' ', s)

# Split by spaces
words = s_clean.split()

# Count words
print(len(words))