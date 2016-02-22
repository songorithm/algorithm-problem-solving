

def getMinCost( aLengthList ) :

    if len(aLengthList) == 1 :
        return 0

    aLengthList.sort();

    sMinCost = aLengthList[0] + aLengthList[1]

    del aLengthList[1]
    del aLengthList[0]

    aLengthList.append( sMinCost )

    return sMinCost + getMinCost( aLengthList )

def solve() :

    sTestCount = input()

    for _ in range( sTestCount ) :
        _ = input()
        sInput = raw_input().split()
        sLengthList = [ int(num) for num in sInput ]

        print getMinCost( sLengthList )

solve()
