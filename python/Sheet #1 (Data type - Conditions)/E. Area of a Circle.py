#input recive
N=int(input())
#hours count
hours= N//3600
#remainder_previous_seconds
remaining_seconds = N % 3600
#minutes count
minutes = remaining_seconds // 60
#seconds
seconds = remaining_seconds % 60

print(f"{hours}:{minutes}:{seconds}")
