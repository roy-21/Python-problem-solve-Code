# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/Q

s = input()

# Split into words
words = s.split(' ')

# Reverse each word
reversed_words = [word[::-1] for word in words]

# Join back with space
print(' '.join(reversed_words))