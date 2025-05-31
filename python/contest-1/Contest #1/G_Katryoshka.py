def max_katryoshkas(n, m, k):
    # Combination 3: 1 eye + 1 mouth + 1 body
    min1 = min(n, m, k)
    n -= min1
    m -= min1
    k -= min1

    # Combination 1: 2 eyes + 1 body
    min2 = min(n // 2, k)

    # Total Katryoshkas
    total = min1 + min2
    return total

# Example Usage
n, m, k = map(int, input().split())
print(max_katryoshkas(n, m, k))
