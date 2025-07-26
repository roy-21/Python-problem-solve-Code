# contest_link__ https://codeforces.com/group/MWSDmqGsZm/contest/219158


# Python program to demonstrate working of 
# extended Euclidean Algorithm 
# Function to return
# gcd of a and b

def findGCD(a, b):
    if a == 0:
        return b
    return findGCD(b % a , a)

#main_funcation 
def main():
    a =int(input())
    b =int(input())
    g = findGCD(a, b)
    print(g)

if __name__ == "__main__":
    main()



#math.gcd() function use kore korte pari

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# # Input
# A, B = map(int, input().split())

# # Output
# print(gcd(A, B))
