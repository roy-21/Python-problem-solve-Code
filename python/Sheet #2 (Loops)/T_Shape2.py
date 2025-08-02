# contest_link__ https://codeforces.com/group/MWSDmqGsZm/contest/219158


N = int(input())

for i in range(1, N + 1):
    spaces = ' ' * (N - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)
