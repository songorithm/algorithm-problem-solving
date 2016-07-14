import sys
graph = None

inf = 987654321

def update(v1, v2, cost, V):
    for i in xrange(V):
        for j in xrange(V):
            graph[i][j] = min(graph[i][j],\
                            min(graph[i][v1] + cost + graph[v2][j],\
                            graph[i][v2] + cost + graph[v1][j]))

def floyd(V):
    for i in xrange(V):
        for j in xrange(V):
            for k in xrange(V):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()
    for _ in xrange(int(rl())):
        V, M, N = map(int, rl().split())
        V += 1
        graph = [[inf]*V for _ in xrange(V)]
        for i in xrange(V):
            graph[i][i] = 0

        for _ in xrange(M):
            v1, v2, cost = map(int, rl().split())
            graph[v1][v2] = cost
            graph[v2][v1] = cost

        count = 0
        for _ in xrange(N):
            v1, v2, cost = map(int, rl().split())
            if graph[v1][v2] <= cost:
                count += 1
                continue

            graph[v1][v2] = graph[v2][v1] = cost
            update(v1,v2,cost,V)

        print(count)
