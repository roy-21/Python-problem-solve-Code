# contest_link__ https://codeforces.com/group/MWSDmqGsZm/contest/219158


N = int(input().strip())
#reverse_string_using_(string-slicing-concept)
#using int bcz leading zero is skip
rev_n = int(str(N)[::-1])

print(rev_n)
if N == rev_n:
    print("YES")
else:
    print("NO")