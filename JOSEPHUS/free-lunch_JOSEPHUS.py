import sys

def solve(n, k):
    list = [i for i in xrange(n)]
    index = 0
    del list[index]

    while len(list) > 2:
        index = (index + (k-1)) % len(list)
        del list[index]

    return list

if __name__ == "__main__":
    rl = lambda: sys.stdin.readline()
    for _ in xrange(int(rl())):
        n, k = rl().split()
        ret = solve(int(n), int(k))
        print ret[0]+1, ret[1]+1