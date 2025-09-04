#Swap minimum and maximum in an array

#Input
N = int(input())  
A = list(map(int, input().split()))  

#Find min and max values and their indices
min_val = min(A)
max_val = max(A)
min_index = A.index(min_val)
max_index = A.index(max_val)

#Swap min and max
A[min_index], A[max_index] = A[max_index], A[min_index]

#Print the modified array
print(" ".join(map(str, A)))
