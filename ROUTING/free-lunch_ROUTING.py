import sys
from heapq import *
import gc

rl = lambda: sys.stdin.readline()

for i in xrange(int(rl())):
    n, m = map(int, rl().split())
    gc.collect()
    e = [[] for _ in xrange(n)]
    for k in xrange(m):
        input = rl().split()
        v1, v2, value = int(input[0]), int(input[1]), float(input[2])
        e[v1].append((v2,value))
        e[v2].append((v1,value))

    start = 0
    end = n - 1

    visited = [False] * n
    dist = [1e200] * n
    q = []
    heappush(q, (1.0,start))

    while q:
        cost, v1 = heappop(q)
        if v1 == end:
            break

        visited[v1] = True

        for v2,c in e[v1]:
            dist[v2] = min(cost * c, dist[v2])
            if not visited[v2]:
                heappush(q,(dist[v2],v2))


    print "{:.10f}".format(dist[end])
