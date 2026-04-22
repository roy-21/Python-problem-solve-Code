#--  https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/D


# Input
A = input().strip()
B = input().strip()

#Print sizes
print(len(A), len(B))

#Concatenate and print
print(A + B)

#Swap first characters
new_A = B[0] + A[1:]
new_B = A[0] + B[1:]

print(new_A, new_B)