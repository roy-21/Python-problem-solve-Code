#https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/S


s = input().strip()

l_count = 0
r_count = 0
current = ""
result = []

for ch in s:
    current += ch
    
    if ch == 'L':
        l_count += 1
    else:
        r_count += 1
    
    # When balanced
    if l_count == r_count:
        result.append(current)
        current = ""
        l_count = 0
        r_count = 0

# Output
print(len(result))
for part in result:
    print(part)