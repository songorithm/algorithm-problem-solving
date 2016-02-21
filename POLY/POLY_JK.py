# POLY
# Jaekyoung Kim (rlakim5521@naver.com)

MOD = 10000000

# Returns a matrix of numbers of polyomino
def getPolyomino(matrix):
    for iter in range(1, 101):
        matrix[iter][iter] = 1
    matrix[1][0] = 1
    
    for row in range(2, 101):
        for col in range(1, row):
            matrix[row][1] = matrix[row][1] + col * matrix[row - 1][col]
        for col in range(2, 101 - row + 1):
            matrix[row + col - 1][col] = matrix[row + col - 2][col - 1] + matrix[row - 1][0]
        for col in range(1, row + 1):
            matrix[row][0] = matrix[row][0] + matrix[row][col]
            
    return matrix

# Create a cache for memoization
matrix = [[0 for col in range(101)] for row in range(101)]

# Gets a matrix of numbers of polyomino
matrix = getPolyomino(matrix)

# Main function
if __name__ == "__main__":
    caseNumber = int(raw_input())
    
    for case in range(caseNumber):
        n = int(raw_input())
        
        print (matrix[n][0] % MOD)
