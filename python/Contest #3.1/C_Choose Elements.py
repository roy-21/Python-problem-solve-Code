# https://codeforces.com/group/MWSDmqGsZm/contest/329103/problem/C


n, k = map(int, input().split())
a = list(map(int, input().split()))

#Sort descending
a.sort(reverse=True)

#Choose top k elements (but ignore negatives)
max_sum = sum(x for x in a[:k] if x > 0)
print(max_sum)