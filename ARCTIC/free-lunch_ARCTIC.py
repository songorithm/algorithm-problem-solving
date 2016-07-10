import sys
import collections

# Visit all vetex using BFS
def decision(stations, power):
    n = len(stations)
    q = collections.deque()

    visited = [False] * n
    q.append(0)
    visited[0] = True

    while q:
        here = q.pop()
        for there in xrange(n):
            if not visited[there]:
                dist = (stations[here][0]-stations[there][0])**2 + (stations[here][1]-stations[there][1])**2
                if dist <= power:
                    visited[there] = True
                    q.append(there)
    return all(visited)


def solve(stations):
    n = len(stations)
    dist_list = set()

    # Calculate all distances
    for i in xrange(n):
        for j in xrange(n):
            if i == j:
                continue
            dist = (stations[i][0]-stations[j][0])**2 + (stations[i][1]-stations[j][1])**2
            dist_list.add(dist)

    # Sort distances
    dist_list = sorted(dist_list)
    low = 0
    high = len(dist_list) -1

    # Search a range of correct answer
    while high - low > 3:
        mid = int(round(low+high)/2)
        if decision(stations, dist_list[mid]):
            high = mid
        else:
            low = mid

    # Search correct answer in range
    for i in xrange(low, high+1):
        if decision(stations, dist_list[i]):
            return round(dist_list[i]**(0.5),2)

if __name__ == "__main__":
    rl = lambda : sys.stdin.readline()

    for _ in xrange(int(rl())):
        stations = []
        for _ in xrange(int(rl())):
            stations.append(map(float, rl().split()))

        print "{:.2f}".format(solve(stations))
