
def compare( aLeft, aRight ) :

    sRC = cmp( aLeft[1], aRight[1] )
    if sRC != 0 :
        return sRC * -1
    else :
        sRC = cmp( aLeft[0], aRight[0] )
        return sRC

def getTime( aLunchList ) :

    sSortedLunchList = sorted( aLunchList,
                               cmp = compare )

    sLeftTime = 0
    sTime = 0

    for sItem in sSortedLunchList :

        sTime = sTime + sItem[0]
        sLeftTime = sLeftTime - sItem[0]

        if sLeftTime < 0 :
            sLeftTime = 0

        if sLeftTime < sItem[1] :
            sLeftTime = sItem[1]

    sTime = sTime + sLeftTime

    return sTime

def solve() :

    sTestCount = input()

    for _ in range( sTestCount ) :
        sList = []
        sParticipantCount = input()

        sWarmTime = raw_input().split()
        sEatTime = raw_input().split()

        for sIndex in range( sParticipantCount ) :
            sItem = ( int(sWarmTime[sIndex]), int(sEatTime[sIndex]) )
            sList.append( sItem )

        print getTime( sList )

solve()
