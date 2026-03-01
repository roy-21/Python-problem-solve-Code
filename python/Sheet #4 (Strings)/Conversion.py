# problem - https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/D


# Input
A = input().strip()
B = input().strip()

#Print sizes
print(len(A), len(B))

#Print concatenation
print(A + B)

# Swap first characters
# Convert to list because strings are immutable in Python
A_list = list(A)
B_list = list(B)

# Swap first character
A_list[0], B_list[0] = B_list[0], A_list[0]

# Convert back to string
A_swapped = "".join(A_list)
B_swapped = "".join(B_list)

print(A_swapped, B_swapped)






# olternative solution without using lists:
    
# A = input().strip()
# B = input().strip()

# print(len(A), len(B))
# print(A + B)
# print(B[0] + A[1:], A[0] + B[1:])