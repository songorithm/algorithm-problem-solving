
gList1 = []
gList2 = []
gList1Count = 0
gList2Count = 0
gJLIS = []

MIN_VALUE = float("-inf")

def getJLIS( aIndex1,
             aIndex2 ) :

    global gList1
    global gList2

    global gList1Count
    global gList2Count

    if gJLIS[aIndex1+1][aIndex2+1] is not 0 :
        return gJLIS[aIndex1+1][aIndex2+1]

    if aIndex1 is -1 :
        sList1Value = MIN_VALUE
    else :
        sList1Value = gList1[aIndex1]

    if aIndex2 is -1 :
        sList2Value = MIN_VALUE
    else :
        sList2Value = gList2[aIndex2]

    sMaxValue = max( sList1Value, sList2Value )
    sJLIS = 2

    for sIndex in range( aIndex1+1, gList1Count ) :
        if sMaxValue < gList1[sIndex] :
            sTempJLIS = getJLIS( sIndex, aIndex2 ) + 1
            if sTempJLIS > sJLIS :
                sJLIS = sTempJLIS

    for sIndex in range( aIndex2+1, gList2Count ) :
        if sMaxValue < gList2[sIndex] :
            sTempJLIS = getJLIS( aIndex1, sIndex ) + 1
            if sTempJLIS > sJLIS :
                sJLIS = sTempJLIS

    gJLIS[aIndex1+1][aIndex2+1] = sJLIS

    return sJLIS

def solve() :
    global gList1
    global gList2

    global gList1Count
    global gList2Count
 
    global gJLIS

    sCount = input()

    for i in range( sCount ) :

        gJLIS = [ [ int(0) for i in range(101) ] for i in range(101) ]

        sInput = raw_input()

        sInput = raw_input().split()
        gList1 = [ int(num) for num in sInput ]
        gList1Count = len( gList1 )

        sInput = raw_input().split()
        gList2 = [ int(num) for num in sInput ]
        gList2Count = len( gList2 )

        print getJLIS( -1, -1 ) - 2

solve();
