# contest_link__ https://codeforces.com/group/MWSDmqGsZm/contest/219158


#test_case
T = int(input())


for _ in range(T):
    N = int(input())
    Binary = bin(N)[2:] #Convert N to binary and remove '0b' prefix
    count_ones = Binary.count('1') #Count the number of ones
    #count_zeros = Binary.count('0')

    new_binary = '1' * count_ones  #Create new binary with count_ones number of '1's
    #new_binary += '0' * count_zeros
    result = int(new_binary, 2)  #Convert new binary to decimal
    print(result)

