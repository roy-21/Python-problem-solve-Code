# contest_link__ https://codeforces.com/group/MWSDmqGsZm/contest/219158


# #use_python_max_funcation

# N = int(input())
# X = list(map(int, input().split()))
# max_numbers = max(X)
# print(max_numbers)


#use_for_loop

N = int(input())
X = list(map(int, input().split()))

max_num = X[0]

for i in X:
    if i > max_num:
        max_num = i

print(max_num)


