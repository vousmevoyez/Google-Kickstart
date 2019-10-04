import collections

# 思路: https://www.xuejiayuan.net/blog/e5e83370aefb4d2ca867eb03bc9968e9
# 曼哈顿距离转切比雪夫距离: https://www.cnblogs.com/SGCollin/p/9636955.html

def min_dist(mat):
    def is_valid(middle):
        a, b = float('-inf'), float('inf')
        c, d = float('-inf'), float('inf')
        found = False
        for i in xrange(m):
            for j in xrange(n):
                if dist[i][j] > middle:
                    found = True
                    a = max(a, i + j)
                    b = min(b, i + j)
                    c = max(c, i - j)
                    d = min(d, i - j)
        if not found: return True
        for i in xrange(m):
            for j in xrange(n):
                if (abs(a - (i + j)) <= middle and 
                        abs(b - (i + j)) <= middle and 
                        abs(c - (i - j)) <= middle and 
                        abs(d - (i - j)) <= middle):
                    return True
        return False

    m, n = len(mat), len(mat[0])
    dist = [[-1] * n for _ in xrange(m)]
    q = collections.deque([])
    for i in xrange(m):
        for j in xrange(n):
            if mat[i][j] == 1:
                dist[i][j] = 0
                q.append((i, j))

    max_dist = 0
    while q:
        x, y = q.popleft()
        max_dist = dist[x][y]
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < m and 0 <= ny < n) or dist[nx][ny] != -1:
                continue
            dist[nx][ny] = max_dist + 1
            q.append((nx, ny))

    right = max_dist+1
    left = 0
    while left < right:
        mid = (left + right) / 2
        if is_valid(mid):
            right = mid
        else:
            left = mid + 1
    return right


T = int(raw_input())
for i in xrange(1, T + 1):
    R, C = map(int, raw_input().split())
    mat = [[0] * C for _ in xrange(R)]
    for row in xrange(R):
        line = raw_input()
        for col in xrange(len(line)):
            mat[row][col] = int(line[col])
    res = min_dist(mat)
    print "Case #{}: {}".format(i, res)

