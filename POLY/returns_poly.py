
gPolyMatrix = [ [ int(0) for i in range(101) ] for i in range(101) ]


def getPolyMatrixValue( aColumn, aTarget ) :

    global gPolyMatrix
    sValue = 0

    for sColumnIndex in range( 1, aTarget - aColumn + 1 ) :
        sTempValue = gPolyMatrix[aTarget-aColumn][sColumnIndex] * ( aColumn + sColumnIndex - 1 )
        sValue = sValue + sTempValue

    return sValue % 10000000

def getPolyValue( aValue ) :

    global gPolyMatrix
    sValue = 0

    for i in range( 1, aValue + 1 ):
        sValue += gPolyMatrix[aValue][i]

    return sValue % 10000000

def getPolyMatrix( aCount ) :

    global gPolyMatrix
    sValue = 0

    for sRowIndex in range( 1, aCount + 1 ) :
        for sColumnIndex in range( 1, sRowIndex + 1 ) :
            if sRowIndex is sColumnIndex :
                sValue = 1
            else :
                sValue = getPolyMatrixValue( sColumnIndex, sRowIndex )

            gPolyMatrix[sRowIndex][sColumnIndex] = sValue

        gPolyMatrix[sRowIndex][0] = getPolyValue( sRowIndex )

def solve() :

    global gPolyMatrix

    sCount = input()

    for i in range( sCount ) :
        sValue = input()

        if gPolyMatrix[sValue][0] is 0 :
            getPolyMatrix( sValue )

        print gPolyMatrix[sValue][0]

solve()
