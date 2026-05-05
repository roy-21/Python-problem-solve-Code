# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/F


# Number of test cases
T = int(input().strip())

for _ in range(T):
    S = input().strip()
    
    if len(S) > 10:
        # First char + count of middle chars + last char
        print(S[0] + str(len(S) - 2) + S[-1])
    else:
        print(S)
        

#olternative solution using string formatting:
# for _ in range(int(input())):
#     s = input().strip()
#     print(s if len(s) <= 10 else f"{s[0]}{len(s)-2}{s[-1]}")