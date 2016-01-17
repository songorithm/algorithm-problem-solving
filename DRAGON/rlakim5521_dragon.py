# DRAGON
# Jaekyoung Kim (rlakim5521@naver.com)

import sys

# Returns a biggest power of two number which is equal to index or smaller than index.
def getNotBigPowerOfTwo(index):
    for exponent in xrange(29):
        if(index - pow(2, exponent) < 0):
            return pow(2, exponent - 1)
    return pow(2, 28)

# Returns '+' or '-'
# There is a rule that a character of (3 * 2^n)th index is '+' and a character of (3 * (2^n + 2^(n-1)))th index is '-'.
# For example,
#  F X + Y F + F X - Y F + F X + Y F - F X - Y F + F X + Y F + F X - Y F - F X + Y F - F X - Y F +
#      3     6     9    12    15    18    21    24    27    30    33    36    39    42    45    48
#  3*2^0 3*2^1       3*2^2                   3*2^3                                           3*2^4
#        3*(2^1+2^0)       3*(2^2+2^1)                         3*(2^3+2^2) 
def getOperator(index):
    notBigPowerOfTwo = getNotBigPowerOfTwo(index)
    
    if(index == 1):
        return "+"
    elif(index == notBigPowerOfTwo + notBigPowerOfTwo / 2):
        return "-"
    elif(index == notBigPowerOfTwo):
        return "+"
    else:
        return getOperator(index - notBigPowerOfTwo)


# Main function
def MainFunction():
    if __name__ == "__main__":
        for _ in xrange(input()):
            # Input
            generationOfDragonCurve, startIndex, numberOfprintedIndex = map(int, raw_input().split())
            
            # Output
            # There is a rule that
            # every character of (6N + 1)th index is 'F' and
            # every character of (6N + 2)th index is 'x' and
            # every character of (6N + 4)th index is 'Y' and
            # every character of (6N + 5)th index is 'F'.
            modIndex = startIndex % 6
            for index in xrange(modIndex, modIndex + numberOfprintedIndex):
                modResult = index % 6
                if(modResult == 1):
                    sys.stdout.write("F")
                elif(modResult == 2):
                    sys.stdout.write("X")
                elif(modResult == 3):
                    sys.stdout.write(getOperator((startIndex + index - modIndex) / 3))
                elif(modResult == 4):
                    sys.stdout.write("Y")
                elif(modResult == 5):
                    sys.stdout.write("F")
                elif(modResult == 0):
                    sys.stdout.write(getOperator((startIndex + index - modIndex) / 3))
            print

MainFunction()
