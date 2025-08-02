# contest_link__ https://codeforces.com/group/MWSDmqGsZm/contest/219158


N = int(input())

# Top half: 1 to N
for i in range(1, N + 1):
    spaces = ' ' * (N - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

# Bottom half: N to 1 (including middle line again)
for i in range(N, 0, -1):
    spaces = ' ' * (N - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)
