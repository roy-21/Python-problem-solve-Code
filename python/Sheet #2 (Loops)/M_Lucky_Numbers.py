# contest_link__ https://codeforces.com/group/MWSDmqGsZm/contest/219158


A, B = map(int, input().split())
# Initialize an empty list to store lucky numbers
lucky_number = []

# Loop through all numbers from A to B (inclusive)
for i in range(A, B + 1):
      # Convert the number to a string and check if all its digits are either '4' or '7'
    if all(digit in "47" for digit in str(i)):
        lucky_number.append(i)  # If lucky, add to the list

    
# Print the lucky numbers if found, otherwise print -1
if lucky_number:
    print(" ".join(lucky_numbers))  # Ensure proper spacing between numbers
else:
    print('-1')  # If no lucky numbers found, print -1


