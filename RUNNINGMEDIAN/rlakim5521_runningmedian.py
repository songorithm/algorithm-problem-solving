# RUNNINGMEDIAN
# Jaekyoung Kim (rlakim5521@naver.com)

from heapq import *

class minHeap():
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def push(self, item):
        self.size = self.size + 1
        heappush(self.heap, item)
        
    def pop(self):
        self.size = self.size - 1
        return heappop(self.heap)
    
    def top(self):
        return self.heap[0]

class maxHeap():
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def push(self, item):
        self.size = self.size + 1
        heappush(self.heap, -1 * item)
        
    def pop(self):
        self.size = self.size - 1
        return -1 * heappop(self.heap)
    
    def top(self):
        return -1 * self.heap[0]

class medianHeap():
    def __init__(self):
        self.bigger = minHeap()
        self.smaller = maxHeap()
        self.size = 0
        
    def push(self, item):
        self.size = self.size + 1
        
        if self.bigger.size == self.smaller.size:
            self.smaller.push(item)
        else:
            self.bigger.push(item)
            
        if self.bigger.size > 0 and self.bigger.top() < self.smaller.top():
            self.bigger.push(self.smaller.pop())
            self.smaller.push(self.bigger.pop())
    
    def getMedian(self):
        return self.smaller.top()
        

# Main function
if __name__ == "__main__":
    for _ in range(int(raw_input())):
        # Input
        N, a, b = map(int, raw_input().split())
        A = [ 0 for _ in xrange(N) ]
        A[0] = 1983
        for _ in xrange(1, N):
            A[_] = (A[_-1] * a + b) % 20090711
        
        # Solve
        ret = 0
        mHeap = medianHeap()
        for _ in xrange(N):
            mHeap.push(A[_])
            ret = ret + mHeap.getMedian()
            
        # Output
        print ret % 20090711
