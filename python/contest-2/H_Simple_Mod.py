
N = int(input())

found = False
for x in range(0, 1001):
    for y in range(0, 1001):
        if (x*x + y*y) % N == 0:
            print(x, y)
            found = True
            break
    if found:
        break

if not found:
    print("No solutions")
