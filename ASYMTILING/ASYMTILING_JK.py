# ASYMTILING
# Jaekyoung Kim (rlakim5521@naver.com)

# Returns a list of all possible numbers of cases of tiles
# when n is 1 to 100
def getAllTiles(allTiles):
    for iter in range(2, 101):
        allTiles[iter] = allTiles[iter - 1] + allTiles[iter - 2]
    
    return allTiles

# Returns a list of all possible numbers of cases of symmetric tiles
# when n is 1 to 100
def getSymmetricTiles(symmetricTiles):
    for iter in range(4, 101):
        symmetricTiles[iter] = symmetricTiles[iter - 2] + symmetricTiles[iter - 4]
        
    return symmetricTiles

# Returns a list of all possible numbers of cases of non-symmetric tiles
# when n is 1 to 100
def getAsymmetricTiles(asymmetricTiles, allTiles, symmetricTiles):
    for iter in range(1, 101):
        asymmetricTiles[iter] = allTiles[iter] - symmetricTiles[iter]

    return asymmetricTiles

# Caches for memoization
asymmetricTiles = [0 for _ in range(101)]
allTiles = [0 for _ in range(101)]
symmetricTiles = [0 for _ in range(101)]


# Sets initial values for allTiles
allTiles[0] = 1
allTiles[1] = 1

# Gets all possible numbers of cases of tiles when n is 1 to 100
allTiles = getAllTiles(allTiles)

# Sets initial values for symmetricTiles 
symmetricTiles[0] = 1
symmetricTiles[1] = 1
symmetricTiles[2] = 2
symmetricTiles[3] = 1

# Gets all possible numbers of cases of symmetric tiles when n is 1 to 100
symmetricTiles = getSymmetricTiles(symmetricTiles)

# Gets all possible numbers of cases of non-symmetric tiles when n is 1 to 100
asymmetricTiles = getAsymmetricTiles(asymmetricTiles, allTiles, symmetricTiles)

# Main function
if __name__ == "__main__":
    caseNumber = int(raw_input())
    
    for iter in range(caseNumber):
        n = int(raw_input())
        
        print (asymmetricTiles[n] % 1000000007)
