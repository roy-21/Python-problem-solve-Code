# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/H

T = int(input().strip())

for _ in range(T):
    S = input().strip()
    
    if "010" in S or "101" in S:
        print("Good")
    else:
        print("Bad")
        
        
# Alternative solution using regular expressions:
# for _ in range(int(input())):
#     s = input().strip()
#     print("Good" if "010" in s or "101" in s else "Bad")