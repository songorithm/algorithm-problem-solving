# DRUNKEN
# Jaekyoung Kim (rlakim5521@naver.com)


def main():
    # Map of Seoul City
    # V : a number of locations
    # E : a number of roads
    V, E = map(int, raw_input().split())
    # crackdown : times for a crackdown on drunk drive
    crackdown = map(int, raw_input().split())
    crackdown = [-1] + crackdown
    # path[(a, b)] = (c, d) : an adjacent list representing c(a time for arriving) and d(an worst crackdown time)
    #                         from a to b
    path = {}
    for road_index in xrange(E):
        a, b, c = map(int, raw_input().split())
        path[(a, b)] = (c, 0)
        path[(b, a)] = (c, 0)

    for k in xrange(V):
        for i in xrange(V):
            for j in xrange(V):
                if (i, k) in path and (k, j) in path:
                    if not (i, j) in path or\
                        sum(path[(i, j)]) > path[(i, k)][0] + path[(k, j)][0] + max(path[(i, k)][1],
                                                                                    path[(k, j)][1],
                                                                                    crackdown[k]):
                        path[(i, j)] = (path[(i, k)][0] + path[(k, j)][0],
                                        max(path[(i, k)][1], path[(k, j)][1], crackdown[k]))

    # Problem
    # T : the number of test cases
    T = int(raw_input())
    for case in xrange(T):
        # s : the location of Hyoseung
        # t : the location where friends are waiting
        s, t = map(int, raw_input().split())

        # Output
        print sum(path[(s, t)])

if __name__ == "__main__":
    main()
