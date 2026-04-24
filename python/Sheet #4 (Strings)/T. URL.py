#https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/T


s = input().strip()

# Get part after '?'
query = s.split('?')[1]

# Split parameters
params = query.split('&')

for p in params:
    key, value = p.split('=')
    print(f"{key}: {value}")