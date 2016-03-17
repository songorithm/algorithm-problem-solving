# NUMB3RS
# Jaekyoung Kim (rlakim5521@naver.com)

# Main function
def MainFunction():
    if __name__ == "__main__":
        for _ in xrange(input()):
            # Input
            numberOfTowns, daysAfterEscaping, townNumberOfPrison = map(int, raw_input().split())
            mapOfTowns = [[0.0] * numberOfTowns for _ in range(numberOfTowns)]
            
            for row in xrange(numberOfTowns):
                mapOfTowns[row] = map(float, raw_input().split())
            
            sumOfCol = [sum(mapOfTowns[col]) for col in range(numberOfTowns)]
            
            for col in xrange(numberOfTowns):
                for row in range(numberOfTowns):
                    mapOfTowns[row][col] = mapOfTowns[row][col] / sumOfCol[col]
            
            numberOfCalculations = int(raw_input())
            townNumberOfCalculatedTown = [0] * numberOfCalculations
            townNumberOfCalculatedTown = map(int, raw_input().split())
            probabilitiesDrDunibalHiding = [[0.0] * numberOfTowns for _ in range(daysAfterEscaping + 1)]
            
            # Sets a initial value
            probabilitiesDrDunibalHiding[0][townNumberOfPrison] = 1.0
            
            # Gets the numbers of cases that Dr. Dunibal hided in each town at each moment
            for dayAfterEscaping in xrange(1, daysAfterEscaping + 1):
                for townNumber in xrange(numberOfTowns):
                    probabilitiesDrDunibalHiding[dayAfterEscaping][townNumber] = \
                    sum([a*b for a,b in zip(probabilitiesDrDunibalHiding[dayAfterEscaping - 1], mapOfTowns[townNumber])])
            
            # Output
            for _ in range(len(townNumberOfCalculatedTown)):
                print probabilitiesDrDunibalHiding[daysAfterEscaping][townNumberOfCalculatedTown[_]],
            print
            
MainFunction()
