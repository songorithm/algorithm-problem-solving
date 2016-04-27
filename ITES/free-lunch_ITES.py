def solve(n, k):
    queue = [0] * 0x400
    tail = head = -1
    s = 0.0
    count = 0
    num = 1983.0
    selfMod = lambda n,k: n - k *int(n/k)

    for _ in xrange(int(n)):
        r = selfMod(num, 10000.0)+1.0
        tail = (tail+1) & 0x3ff
        queue[tail] = r
        s += r
        num = num * 214013.0 + 2531011.0
        num = selfMod(num, 4294967296.0)

        for _ in xrange(1024):
            if s < k:
                break
            elif s == k:
                count += 1
                break
            else:
                head += 1
                head &= 0x3ff
                s -= queue[head]

    print count

if __name__ == "__main__":
    C = int(raw_input())
    for _ in xrange(C):
        rl = raw_input()
        input = rl.split()
        solve(float(input[1]), float(input[0]))
