//
//  main.cpp
//  Poly
//
//  Created by DooSeon Choi on 2014. 8. 24..
//  Copyright (c) 2014³â DoO. All rights reserved.
//

#include <iostream>

long gPolyMatrix[100][100];

long getPolyMatrixValue( int aColulmn, int aTarget )
{
    int sColumnIndex = 0;
    long sValue = 0;
    
    for ( sColumnIndex = 1; sColumnIndex <= aTarget - aColulmn; sColumnIndex++ )
    {
        sValue += gPolyMatrix[aTarget - aColulmn][sColumnIndex] * ( aColulmn + sColumnIndex - 1 );
    }
    
    return sValue % 10000000;
}

long getPolyValue( int aValue )
{
    long sValue = 0;
    int sIndex = 0;
    
    for ( sIndex = 1; sIndex < aValue + 1; sIndex++ )
    {
        sValue += gPolyMatrix[aValue][sIndex];
    }
    
    return sValue % 10000000;
}

void makePolyMatrix( int aCount )
{
    int sRowIndex = 0;
    int sColulmnIndex = 0;
    long sValue = 0;
    
    for ( sRowIndex = 1; sRowIndex < aCount + 1; sRowIndex++ )
    {
        for ( sColulmnIndex = 1; sColulmnIndex < sRowIndex + 1; sColulmnIndex++ )
        {
            if ( sRowIndex == sColulmnIndex )
            {
                gPolyMatrix[sRowIndex][sColulmnIndex] = 1;
            }
            else
            {
                sValue = getPolyMatrixValue( sColulmnIndex, sRowIndex );
                gPolyMatrix[sRowIndex][sColulmnIndex] = sValue;
            }
        }
        
        gPolyMatrix[sRowIndex][0] = getPolyValue( sRowIndex );
    }
}

int main(int argc, const char * argv[])
{
    int sCount = 0;
    int sValue = 0;
    int sIndex = 0;
    
    scanf("%d", &sCount );
    
    makePolyMatrix( 100 );
    
    for ( sIndex = 0; sIndex < sCount; sIndex ++ )
    {
        scanf("%d", &sValue );
        /*
        if ( gPolyMatrix[sValue][0] != 0 )
        {
        }
        else
        {
            makePolyMatrix( sValue );
        }
         */
        
        printf("%ld\n", gPolyMatrix[sValue][0] );
    }
    
    return 0;
}
