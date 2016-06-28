import sys

UNWATCHED = 0
WATCHED = 1
INSTALLED = 2

class DFS():
    def __init__(self,visited, adj, installed):
        self.visited = visited
        self.adj = adj
        self.installed = 0

    def dfs(self,here):
        self.visited[here] = True
        children = [0] * 3
        for there in self.adj[here]:
            if not self.visited[there]:
                children[self.dfs(there)] += 1

        if children[UNWATCHED] != 0:
            self.installed += 1
            return INSTALLED

        if children[INSTALLED] != 0:
            return WATCHED
        return UNWATCHED

    def getInstalled(self):
        return self.installed

    def printAll(self):
        print self.visited
        print self.adj
        print self.installed

def solve(G, H, connected):

    visited = [False] * G
    installed = 0

    adj = [[] for _ in xrange(G)]
    for c in connected:
        adj[c[0]].append(c[1])
        adj[c[1]].append(c[0])

    d = DFS(visited, adj, installed)


    for i in xrange(G):
        if not visited[i] and d.dfs(i) == UNWATCHED:
            installed += 1


    return installed + d.getInstalled()


if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()
    for _ in xrange(int(rl())):
        G,H = map(int,rl().split())
        connected = []
        for _ in xrange(H):
            connected.append(map(int, rl().split()))
        print solve(G, H, connected)
