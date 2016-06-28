# GALLERY
# Jaekyoung Kim (rlakim5521@naver.com)

import sys
from Queue import Queue
input = sys.stdin.readline

class DominatingSet:
    def __init__(self, g, h):
        # adjList : a graph representing connections of galleries
        # trees : a list of trees
        self.num_of_node = g
        self.num_of_edge = h
        self.adjList = [[] for _ in xrange(g)]
        self.trees = []
        self.visited = [ False ] * g
        
    def insertEdge(self, nodes):
            self.adjList[nodes[0]].append(nodes[1])
            self.adjList[nodes[1]].append(nodes[0])
            
    def bfs(self, node):
        if not self.visited[node]:
            self.visited[node] = True
            child_iter = 1
            tree = []
            
            treeNode = [0]
            for child in self.adjList[node]:
                if not self.visited[child]:
                    treeNode.append(child_iter)
                    child_iter += 1
            tree.append(treeNode)
            
            children_queue = Queue()
            parent_queue = Queue()
            for child in self.adjList[node]:
                children_queue.put(child)
                parent_queue.put(node)
                
            while(not children_queue.empty()):
                current = children_queue.get()
                parent = parent_queue.get()
                if not self.visited[current]:
                    self.visited[current] = True
                    
                    treeNode = [parent]
                    for child in self.adjList[current]:
                        if not self.visited[child]:
                            treeNode.append(child_iter)
                            child_iter += 1
                            children_queue.put(child)
                            parent_queue.put(current)
                    tree.append(treeNode)
                    
            self.trees.append(tree)
                    
    def turnTree(self):
        self.visited = [ False ] * self.num_of_node
        for node in xrange(self.num_of_node):
            self.bfs(node)
        #print self.trees
        #print
    
    def getNumberOfDominatingNode(self, tree):
        # If there is no other node without root, return 1.
        if len(tree) == 1:
            return 1
        
        result = 0
        dominated = [False] * len(tree)
        for iter in xrange(len(tree)-1, -1, -1):
            for child in tree[iter][1:]:
                if dominated[child] == False:
                    # select the current node
                    # turn the current node and parent node to be dominated
                    # we don't need to turn children nodes
                    dominated[tree[iter][0]] = True
                    dominated[iter] = True
                    result += 1
                    break
        
        return result
    
    def solve(self):
        result = 0
        self.turnTree()
        for tree in self.trees:
            result += self.getNumberOfDominatingNode(tree)
        
        return result

if __name__ == "__main__":
    for _ in xrange(int(input())):
        # Input
        # g : the number of galleries    (1<=g<=1000)
        # h : the number of halls        (0<=h<g)
        g, h = map(int, input().split())
        DS = DominatingSet(g, h)
        for _ in xrange(h):
            DS.insertEdge(map(int, input().split()))
        
        # Output
        print DS.solve()
