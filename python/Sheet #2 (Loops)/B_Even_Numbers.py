# contest_link__ https://codeforces.com/group/MWSDmqGsZm/contest/219158


N = int(input())
found = False  # Track korar jonno je even number paoa gelo kina

for i in range(1, N + 1):  # 1 theke N porjonto loop
    if i % 2 == 0:  # Even number check
        print(i)
        found = True  # Jodi even number pai, tahole flag true kore dibo

if not found:  # Jodi kono even number na thake
    print(-1)




# N = int(input())  

# evens = list(range(2, N + 1, 2))  # Direct even numbers list banai
# if evens:  # Jodi list e even number thake
#     print("\n".join(map(str, evens)))  # Prottek even number print kori
# else:
#     print(-1)  # Kono even number na thakle -1 print kori