
import sys

rl = lambda : sys.stdin.readline()


class Graph():


    def __init__(self, number_of_place):
        self.graph = [ [ sys.maxint] * number_of_place for _ in xrange(number_of_place) ]
        self.number_of_place = number_of_place

    def add_edge(self, start_point, end_point, time):
        self.graph[start_point][end_point] = time
        self.graph[end_point][start_point] = time

    def dijkstra(self, start,end):
        visited = [ 0 ] * self.number_of_place
        dist = [ sys.maxint ] * self.number_of_place
        dist[start] = 0
        v = 0

        for index in xrange(1,self.number_of_place):
            min_node = sys.maxint
            for inner_index in xrange(1, self.number_of_place):
                if visited[inner_index] == 0 and min_node > dist[inner_index]:
                    min_node = dist[inner_index]
                    v = inner_index

            visited[v] = True

            for inner_index in xrange(1, self.number_of_place):
                if dist[inner_index] > dist[v] + self.graph[v][inner_index]:
                    dist[inner_index] = dist[v] + self.graph[v][inner_index]

        return dist[end]


def main():
    for tc in xrange(int(rl())):
        place, edge, fires, fire_stations = map(int, rl().rstrip().split())
        graph = Graph(place + 1)
        for _ in xrange(edge):
            start_point, end_point, time = map(int, rl().rstrip().split())
            graph.add_edge(start_point, end_point, time)
        fired_place_list = map(int, rl().rstrip().split())
        fire_station_list = map(int, rl().rstrip().split())

        sum = 0

        for fire_station in fire_station_list:
            graph.add_edge(0,fire_station, 0)

        for fire in fired_place_list:
            sum += graph.dijkstra(0,fire)

        print sum

if __name__ == "__main__":
     main()
