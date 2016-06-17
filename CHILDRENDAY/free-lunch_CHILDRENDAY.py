import sys
import collections

def append(here, edge, mod):
    there = here * 10 + edge
    if there >= mod:
        return there % mod + mod
    return there % mod

def solve(digits, N, M):
    d = dict()
    q = collections.deque()
    digits = sorted(digits)

    here = 0
    d[0] = 0,0
    q.append(0)

    while len(q):
        here = q.popleft()
        for i in digits:
            there = append(here, i, N)
            if not there in d:
                d[there] = here, i
                q.append(there)

    here = N + M
    ret =''
    if not here in d:
        return 'IMPOSSIBLE'

    while d[here][0] != here:
        ret += str(d[here][1])
        here = d[here][0]

    return ret[::-1]

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()
    for _ in xrange(int(rl())):
        digits, N, M = rl().split()
        N = int(N)
        M = int(M)
        digits = map(int, list(digits))
        print solve(digits, N, M)
