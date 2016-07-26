import sys

graph = [[-1]*2000 for _ in xrange(2000)]

def dfs1(n, start, min_v, max_v):
    if start == n-1:
        graph[start][start] = min(graph[start][start], max_v-min_v)
        return

    graph[start][start] = 1
    for i in xrange(n):
        if start == i:
            continue
        # Visited Node
        if n-1 != i and graph[i][i] != -1:
            continue

        if graph[start][i] >= 0:
            if min_v == -1:
                dfs1(n, i, graph[start][i], graph[start][i])
            else:
                dfs1(n,i,min(min_v,graph[start][i]), max(max_v,graph[start][i]))

    graph[start][start] = -1

def solve1(n, m):
    dfs(n, 0, -1, -1)
    return graph[n-1][n-1]

def dfs2(n, start, min_v, max_v):
    if start == n-1:
        return True

    # Check visited
    graph[start][start] = 1
    for i in xrange(n):
        # Visit not visted adjacent node
        if graph[i][i] == -1 and min_v <= graph[start][i] <= max_v:
            if dfs2(n, i, min_v, max_v):
                graph[start][start] = -1
                return True
    graph[start][start] = -1
    return False

def solve2(n, m, orders):
    lo, hi, ret = 0, 0, sys.maxint
    while True:
        if dfs2(n, 0, orders[lo], orders[hi]):
            ret = min(ret, orders[hi]-orders[lo])
            lo += 1
        else:
            if hi == len(orders)-1:
                break
            hi += 1
    return ret

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline().rstrip(' \t\r\n\0')
    for _ in xrange(int(rl())):
        n, m = map(int, rl().split())
        if m == 1:
            rl()
            print(0)
            continue

        for i in xrange(n):
            for j in xrange(n):
                graph[i][j] = -1

        orders = set()
        for i in xrange(m):
            v1, v2, cost = map(int, rl().split())
            graph[v1][v2] = cost
            graph[v2][v1] = cost
            orders.add(cost)

        print(solve2(n, m, sorted(list(orders))))
