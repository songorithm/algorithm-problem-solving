import sys

class CanadaTrip:
    class City:
        def __init__(self, L=0, M=0, G=0):
            self.location = L
            self.meter = M
            self.gap =G

    def __init__(self):
        self.cityList = []
        self.min = sys.maxint
        self.max = 0

    def insert(self, location, meter, gap):
        self.cityList.append(self.City(location, meter, gap))
        self.min = min(self.min, location-meter)
        self.max = max(self.max, location)

    def decision(self, dist):
        ans = 0
        for city in self.cityList:
            startPoint = city.location-city.meter
            if startPoint > dist :
                continue
            remainDist = min(dist, city.location) - startPoint
            ans += remainDist / city.gap + 1
        return ans

    def search(self, number):
        start,end  = self.min, self.max
        while start <= end :
            mid = (start + end ) / 2
            ans = self.decision(mid)
            if ans < number:
                start = mid +1
            else:
                end = mid -1
        return start

if __name__ == "__main__":
    rl = lambda: sys.stdin.readline()
    retList = []
    for _ in xrange(int(float((rl())))):
        input =  [int(n) for n in rl().split()]
        cityNum, tagetNum = input[0], input[1]
        trip = CanadaTrip()

        for _ in xrange(cityNum):
            input =  [int(n) for n in rl().split()]
            location, meter, gap = input[0], input[1], input[2]
            trip.insert(location, meter, gap)

        retList.append(trip.search(tagetNum))

    for ret in retList:
        print ret