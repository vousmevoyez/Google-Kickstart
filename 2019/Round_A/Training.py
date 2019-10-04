def min_time(N, P, arr):
    cum = [0] * N
    arr.sort()
    cum[0] = arr[0]
    for i in xrange(1, len(arr)):
        cum[i] = cum[i - 1] + arr[i]
    res = float('inf')
    for j in xrange(P - 1, len(arr)):
        total = cum[j] - cum[j - P] if j >= P else cum[j]
        res = min(res, arr[j] * P - total)
    return res


T = int(raw_input())
for x in range(1, T + 1):
    N, P = map(int, raw_input().split())
    S = map(int, raw_input().split())
    res = min_time(N, P, S)
    print "Case #{}: {}".format(x, res)
