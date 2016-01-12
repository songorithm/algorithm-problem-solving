
class City :
    def __init__( self, aID ) :
        self.mID = aID
        self.mConnectCityList = []
        self.mConnectCityCount = 0

    def addConnectCity( self, aID ) :
        self.mConnectCityList.append( aID )
        self.mConnectCityCount = self.mConnectCityCount + 1

    def getID( self ) :
        return self.mID

    def getConnectCityCount( self ) :
        return self.mConnectCityCount

    def getConnectCityList( self ) :
        return self.mConnectCityList


def printDebug( aList ) :
    sStr = ''
    for i in range( len(aList) ) :
        if aList[i] != 0 :
            sStr = sStr + " Index: " + str(i) + " Data: " + str(aList[i]) + " "

    print sStr

def getChanceRate( aCityList,
                   aCityIndex,
                   aChance ) :

    sBaseCity = aCityList[aCityIndex]
    sConnectCityList = sBaseCity.getConnectCityList();
    sChanceList = [ 0.0 ] * len( aCityList )

    for sIndex in range( len(sConnectCityList) ) :
        sCityIndex = sConnectCityList[sIndex]
        sID = aCityList[sCityIndex].getID()
        sChance = aChance / sBaseCity.getConnectCityCount()
        sChanceList[sID] = sChance

    return sChanceList


def getChanceList( aCityList,
                   aRemainDay,
                   aChanceList ) :

    if aRemainDay == 0 :
        return aChanceList

    sSumChanceList = [ 0.0 ] * len( aCityList )

    for sCityIndex in range( len(aChanceList) ) :
        if ( aChanceList[sCityIndex] != 0 ) :

            sChanceList = getChanceRate( aCityList,
                                         sCityIndex,
                                         aChanceList[sCityIndex] )

            sSumChanceList = [ n1 + n2 for n1, n2 in zip( sSumChanceList, sChanceList ) ]

    return getChanceList( aCityList, aRemainDay-1, sSumChanceList )

def solve( ) :
    sTestCaseCount = input()

    for i in range( sTestCaseCount ) :

        sInput = raw_input()
        sInputList = sInput.split()

        sRowCount = int( sInputList[0] )
        sRemainDay = int( sInputList[1] )
        sStartCity = int( sInputList[2] )

        sCityList = [ 0 ] * sRowCount

        for sRowIndex in range( sRowCount ) :
            sInput = raw_input()
            sInputList = sInput.split()

            sCity = City( int(sRowIndex) )

            for sColumnIndex in range( sRowCount ) :
                sTempIndex = int( sInputList[sColumnIndex] )
                if  sTempIndex != 0 :
                    sCity.addConnectCity( sColumnIndex )

            sCityList[sRowIndex] = sCity

        sChanceList = getChanceRate( sCityList,
                                     sStartCity,
                                     1.0 )

        sChanceList =  getChanceList( sCityList,
                                      sRemainDay - 1,
                                      sChanceList )

        sOutputCout = input()
        sInput = raw_input()
        sInputList = sInput.split()

        print ' '.join( format( sChanceList[int(sItem)], '.8f' ) for sItem in sInputList )

solve()
