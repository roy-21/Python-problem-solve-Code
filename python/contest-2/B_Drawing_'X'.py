contest-link:- https://codeforces.com/group/MWSDmqGsZm/contest/326907

n = int(input())

# Loop through each row
for i in range(n):
    row = ""
    # Loop through each column in the current row
    for j in range(n):
        if i == j and i == n - 1 - j:
            row += "X"      # This is the exact center of the grid
        elif i == j:
            row += "\\"     # Backslash on the main diagonal
        elif i == n - 1 - j:
            row += "/"      # Slash on the secondary diagonal
        else:
            row += "*"      # Fill all other positions with asterisks
    print(row)               # Print the completed row
         

        
  
