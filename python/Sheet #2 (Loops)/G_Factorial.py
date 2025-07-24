# contest_link__ https://codeforces.com/group/MWSDmqGsZm/contest/219158


# #solve way-01
# #Recursive function for determining factorial

# def factorial(n):
#     if n == 0:  
#         return 1  # বেস কেস: 0! = 1
#     return n * factorial(n - 1)  # রিকার্সিভ কল

# # টেস্ট কেস সংখ্যা ইনপুট
# T = int(input())  

# # প্রতিটি টেস্ট কেসের জন্য ফ্যাক্টোরিয়াল বের করা
# for _ in range(T):
#     N = int(input())  
#     print(factorial(N))  # রিকার্সিভ ফাংশন ব্যবহার করে ফ্যাক্টোরিয়াল বের করা




# #solve way-02
# #using loop

# # ফ্যাক্টোরিয়াল ফাংশন (লুপ ব্যবহার করে)
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):  
#         result *= i  
#     return result  

# # ইনপুট নেওয়া
# T = int(input())  

# for _ in range(T):
#     N = int(input())  
#     print(factorial(N))  # কাস্টম ফাংশন ব্যবহার করে ফ্যাক্টোরিয়াল বের করা


#solve way-03

import math  # ফ্যাক্টোরিয়াল গণনার জন্য লাইব্রেরি ইমপোর্ট

# প্রথম ইনপুট: টেস্ট কেস সংখ্যা T
T = int(input())  

# প্রতিটি টেস্ট কেসের জন্য ফ্যাক্টোরিয়াল বের করা
for _ in range(T):  
    N = int(input())  # সংখ্যা N ইনপুট নেওয়া
    print(math.factorial(N))  # ফ্যাক্টোরিয়াল বের করে প্রিন্ট করা

