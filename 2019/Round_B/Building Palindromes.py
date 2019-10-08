def num_palin(n, q, qry, ss):
    def is_valid(arr):
        return sum(map(lambda x: 1 if x % 2 == 1 else 0, arr)) <= 1

    dic = [[0] * 26 for _ in xrange(n)]
    for i, c in enumerate(ss):
        if i == 0:
            dic[0][ord(c)-ord('A')] += 1
            continue
        for j in xrange(26):
            if j != ord(c)-ord('A'):
                dic[i][j] = dic[i-1][j]
            else:
                dic[i][j] = dic[i-1][j] + 1
    res = 0
    for s, e in qry:
        s -= 1; e -= 1
        if s == 0:
            res += is_valid(dic[e])
        else:
           res += is_valid([a - b for a, b in zip(dic[e], dic[s - 1])])
    return res

T = int(raw_input())

for i in xrange(1, T+1):
    N, Q = map(int, raw_input().split())
    S = raw_input()
    qry = []
    for j in xrange(Q):
        qry.append(map(int, raw_input().split()))
    res = num_palin(N, Q, qry, S)
    print "Case #{}: {}".format(i, res)
