# contest_link__ https://codeforces.com/group/MWSDmqGsZm/contest/219158


N = int(input())
numbers = list(map(int,input().split()))

even_count = 0
odd_count = 0
positive_count = 0
negative_count = 0

for i in numbers:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    
    if i > 0:
        positive_count += 1
    elif i < 0:
        negative_count += 1
    
print(f"Even: {even_count}")
print(f"Odd: {odd_count}")
print(f"Positive: {positive_count}")
print(f"Negative: {negative_count}")