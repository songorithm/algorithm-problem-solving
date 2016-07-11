import sys

def solve(n,m,menu):
    max_value = 0
    if m > 400:
        best = menu[0]
        # print menu
        x, y = divmod(m-400,best[1])
        max_value = best[2] * (x+1)
        m -= best[1] * (x+1)

    cache = [0] * 401
    ret = 0
    for budget in xrange(1,m+1):
        result = 0
        for r, c, p in menu:
            if budget >= c:
                result = max(result, cache[(budget-c)%401] + p)
        cache[budget%401] = result

    return cache[m] + max_value


if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()
    for _ in  xrange(int(rl())):
        n, m = map(int, rl().split())
        m = int(m/100)
        menu = [()]*n
        for i in xrange(n):
            c, p = map(int, rl().split())
            c = int(c/100)
            r = 1.0*c/p
            menu[i] = r,c,p
        menu = sorted(menu)
        print solve(n,m,menu)
