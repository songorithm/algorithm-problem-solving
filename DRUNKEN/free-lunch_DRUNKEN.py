import sys

def solve(v, adj, delay):
    order = sorted(range(v), key=lambda k: delay[k])
    for w in order:
        for i in xrange(v):
            if adj[i][w] == sys.maxint:
                continue
            for j in xrange(v):
                if i == j:
                    continue
                adj[i][j] = min(adj[i][j], adj[i][w]+adj[w][j])
                time[i][j] = min(time[i][j] , adj[i][w] + adj[w][j] + delay[w])

if __name__ == "__main__":
    global time

    rl = lambda: sys.stdin.readline()
    v, e = map(int, rl().split())
    delay = map(int, rl().split())

    adj = [[sys.maxint]*v for _ in xrange(v)]
    time = [[sys.maxint]*v for _ in xrange(v)]

    for _ in xrange(e):
        v1, v2, cost = map(int, rl().split())
        v1 -= 1
        v2 -= 1
        adj[v1][v2] = cost
        adj[v2][v1] = cost
        time[v1][v2] = cost
        time[v2][v1] = cost

    for i in xrange(v):
        time[i][i] = 0

    solve(v, adj, delay)

    for _ in xrange(int(rl())):
        v1, v2  = map(int, rl().split())
        print(time[v1-1][v2-1])
