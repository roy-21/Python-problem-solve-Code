# https://codeforces.com/group/MWSDmqGsZm/contest/329103/problem/F

def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    left = 0
    right = n - 1
    result = []
    while left <= right:
        result.append(str(arr[left]))
        left += 1
        if left <= right:
            result.append(str(arr[right]))
            right -= 1
    print(" ".join(result))

if __name__ == "__main__":
    main()