# contest_link__ https://codeforces.com/group/MWSDmqGsZm/contest/219158


#Read the first line, which contains the symbol (one of +, -, *, /)
S = input().strip() # Using strip() to remove any accidental spaces or newlines

#Read the second line, which contains the number of elements (N)
N = int(input().strip()) # Converting input string to an integer

#Read the third line, which contains N numbers
numbers = list(map(int, input().split())) # Converting input string numbers to a list of integers


# Loop through each number in the list
for i in numbers:
 print(S * i) # Print the symbol repeated num times
