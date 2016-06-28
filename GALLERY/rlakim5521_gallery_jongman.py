# GALLERY
# Jaekyoung Kim (rlakim5521@naver.com)

import sys
input = sys.stdin.readline

UNWATCHED = 0
WATCHED = 1
INSTALLED = 2

def dfs(adj, visited, here):
    visited[here] = True
    children = [0, 0, 0]
    installed = 0
    for i in xrange(len(adj[here])):
        there = adj[here][i]
        if not visited[there]:
            pair = dfs(adj, visited, there)
            children[pair[0]] += 1
            installed += pair[1]
            
    if children[UNWATCHED]:
        installed += 1
        return (INSTALLED, installed)
    
    if children[INSTALLED]:
        return (WATCHED, installed)
    
    return (UNWATCHED, installed)

if __name__ == "__main__":
    for _ in xrange(int(input())):
        # Input
        # g : the number of galleries    (1<=g<=1000)
        # h : the number of halls        (0<=h<g)
        g, h = map(int, input().split())
        adj = [[] for _ in xrange(g)]
        visited = [ False ] * g
        installed = 0
        for _ in xrange(h):
            gallery_1, gallery_2 = map(int, input().split())
            adj[gallery_1].append(gallery_2)
            adj[gallery_2].append(gallery_1)
            
        for u in xrange(g):
            if not visited[u]:
                result = dfs(adj, visited, u)
                installed += result[1]
                if result[0] == UNWATCHED:
                    installed += 1
        
        # Output
        print installed
