#https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/U

s = input().strip().lower()

# Count required letters
count_e = s.count('e')
count_g = s.count('g')
count_y = s.count('y')
count_p = s.count('p')
count_t = s.count('t')

# Result
result = min(count_e, count_g, count_y, count_p, count_t)

print(result)