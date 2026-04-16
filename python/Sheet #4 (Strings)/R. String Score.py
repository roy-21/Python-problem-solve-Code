# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/R

from collections import deque

n = int(input())
s = deque(input().strip())

score = 0

while s:
    ch = s.popleft()

    if ch == 'V':
        score += 5

    elif ch == 'W':
        score += 2

    elif ch == 'X':
        if s:
            s.popleft()  # remove next

    elif ch == 'Y':
        if s:
            s.append(s.popleft())  # move next to end

    elif ch == 'Z':
        if s:
            if s[0] == 'V':
                score //= 5
                s.popleft()
            elif s[0] == 'W':
                score //= 2
                s.popleft()

# Output
print(score)