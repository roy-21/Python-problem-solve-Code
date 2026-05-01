#https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/W

# Input
Q = int(input().strip())
S = input().strip()

Key = "PgEfTYaWGHjDAmxQqFLRpCJBownyUKZXkbvzIdshurMilNSVOtec#@_!=.+-*/"
Original = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Create mappings
encrypt_map = {Original[i]: Key[i] for i in range(len(Original))}
decrypt_map = {Key[i]: Original[i] for i in range(len(Key))}

# Process
result = []

if Q == 1:
    for ch in S:
        result.append(encrypt_map[ch])
else:
    for ch in S:
        result.append(decrypt_map[ch])

# Output
print("".join(result))