import sys
import gc
import collections
"""
v : number of galaxy
w : number of wormhole
e : wormhole graph
"""
def solve(v, w, e, reachable):
    gc.collect()
    dist = [sys.maxint] * v

    dist[0] = 0
    for k in xrange(v-1):
        for here in xrange(v):
            for there, cost in e[here]:
                if dist[there] > dist[here] + cost:
                    dist[there] = dist[here] + cost

    for here in xrange(v):
        for there, cost in e[here]:
            if dist[there] > dist[here] + cost:
                if reachable[0][here] and reachable[here][1]:
                    return sys.maxint

    return dist[1]


if __name__ == "__main__":
    rl = lambda: sys.stdin.readline()

    for i in xrange(int(rl())):
        v, w = map(int, rl().split())
        e = [[]  for _ in xrange(v)]
        e_neg = [[] for _ in xrange(v)]
        reachable = [[False] * v for _ in xrange(v)]
        for i in xrange(v):
            reachable[i][i] = True

        for _ in xrange(w):
            i, j, value = map(int, rl().split())
            e[i].append((j,value))
            e_neg[i].append((j,-value))
            reachable[i][j] = True

        for k in xrange(v):
            for i in xrange(v):
                for j in xrange(v):
                    reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])

        if not reachable[0][1] :
            print 'UNREACHABLE'
            continue


        ret1 = solve(v,w,e,reachable)
        ret2 = -solve(v,w,e_neg,reachable)
        max_value = 10**10
        if ret1 > max_value:
            ret1 = 'INFINITY'
        if abs(ret2) > max_value:
            ret2 = 'INFINITY'

        print ret1, ret2
