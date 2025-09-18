# https://codeforces.com/group/MWSDmqGsZm/contest/329103/problem/E

def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    
    pattern1_flips = 0
    pattern2_flips = 0
    
    for i in range(n):
        if i % 2 == 0:
            if arr[i] < 0:
                pattern1_flips += 1
            if arr[i] > 0:
                pattern2_flips += 1
        else:
            if arr[i] > 0:
                pattern1_flips += 1
            if arr[i] < 0:
                pattern2_flips += 1
                
    print(min(pattern1_flips, pattern2_flips))

if __name__ == "__main__":
    main()