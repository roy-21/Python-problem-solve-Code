def can_form_interval(a, b):
    # If there are no numbers at all, return NO
    if a == 0 and b == 0:
        print("NO")
        return

    # If only one type of number exists but more than one count, it's impossible
    if (a == 0 and b > 0) or (b == 0 and a > 0):
        print("NO")
        return

    # If the difference between a and b is more than 1, it's impossible to alternate
    if abs(a - b) > 1:
        print("NO")
    else:
        print("YES")

# Read input
a, b = map(int, input().split())
can_form_interval(a, b)
