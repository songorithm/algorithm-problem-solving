# MORDOR
# Jaekyoung Kim (rlakim5521@naver.com)

# Main function
if __name__ == "__main__":
    for _ in range(int(raw_input())):
        N, Q = map(int, raw_input().split())
        h = map(int, raw_input().split())
        for _ in xrange(Q):
            a, b = map(int, raw_input().split())
            max = -1
            min = 20001
            for iter in xrange(a, b+1):
                if h[iter] > max:
                    max = h[iter]
                if h[iter] < min:
                    min = h[iter]
            print max - min
