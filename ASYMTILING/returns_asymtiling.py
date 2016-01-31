
gTileCount = [ int(0) for i in range(101) ]

def getAllCount( aTileCount ) :
    global gTileCount

    if gTileCount[aTileCount] is not 0 :
        return gTileCount[aTileCount]

    gTileCount[aTileCount] = ( getAllCount( aTileCount-1 ) + getAllCount( aTileCount-2 ) )

    return gTileCount[aTileCount]

def getSymTilingCount( aTileCount ) :

    if aTileCount % 2 is 1 :
        return getAllCount( (aTileCount - 1) / 2 )
    else :
        return ( getAllCount( aTileCount / 2 ) + getAllCount( (aTileCount-2) / 2 ) )

def getAsymTilingCount( aTileCount ) :
    return ( getAllCount( aTileCount ) - getSymTilingCount( aTileCount ) ) % 1000000007


def solve() :

    global gTileCount

    # Base Data
    gTileCount[0] = 1 # fake 
    gTileCount[1] = 1
    gTileCount[2] = 2

    sCount = input()

    for i in range( sCount ) :
        sTileCount = input()
        print getAsymTilingCount( sTileCount )

solve()
