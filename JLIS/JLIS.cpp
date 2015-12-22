#include <stdio.h>
#include <string.h>

int gList1[100];
int gList2[100];

int gList1Count = 0;
int gList2Count = 0;

int gJLIS[101][101];

long MIN = -2147483647;

int getJLIS( int       aIndex1,
             int       aIndex2 )
{
    int i = 0;
    int j = 0;
    int sJLIS = 0;
    int sTempJLIS = 0;
    long sMaxValue = 0;
    long sList1Value = 0;
    long sList2Value = 0;

    /* already get it */
    if ( gJLIS[aIndex1+1][aIndex2+1] != 0 )
    {
        //printf ( "aIndex1 %d aIndex2 %d return %d\n", aIndex1, aIndex2, gJLIS[aIndex1+1][aIndex2+1] );
        return gJLIS[aIndex1+1][aIndex2+1];
    }

    if ( aIndex1 == -1 )
    {
        sList1Value = MIN;
    }
    else
    {
        sList1Value = gList1[aIndex1];
    }
    
    if ( aIndex2 == -1 )
    {
        sList2Value = MIN;
    }
    else
    {
        sList2Value = gList2[aIndex2];
    }

    /* get max value */
    if ( sList1Value < sList2Value )
    {
        sMaxValue = sList2Value;
        sJLIS = 2;
    }
    else if ( sList1Value > sList2Value )
    {
        sMaxValue = sList1Value;
        sJLIS = 2;
    }
    else
    {
        sMaxValue = sList1Value;
        sJLIS = 1;
    }

    //gJLIS[aIndex1+1][aIndex2+1] = sJLIS;
    //printf( "Index1 %d Value %d  Index2 %d Value %d \n", aIndex1, gList1[aIndex1],aIndex2, gList2[aIndex2] );

    /* list 1 */
    for ( i = aIndex1+1; i < gList1Count; i++ )
    {
        //printf( "MaxValue %d, Index %d, value %d\n", sMaxValue, i, gList1[i] );
        if ( sMaxValue < gList1[i] )
        {
            sTempJLIS = getJLIS( i, aIndex2 ) + 1;
            //printf( " i : %d, aIndex2 : %d, sTempJLIS : %d JLIS %d\n", i, aIndex2, sTempJLIS, sJLIS );
            if ( sTempJLIS > sJLIS )
            {
                sJLIS = sTempJLIS;
                //gJLIS[aIndex1+1][aIndex2+1] = sJLIS;
                //printf ( "List 1 Set JLIS aIndex1 %d aIndex2 %d JLIS %d i :%d\n", aIndex1, aIndex2, sJLIS, i );
            }
        }
    }

    /* list 2 */
    for ( i = aIndex2+1; i < gList2Count; i++ )
    {
        //printf( "MaxValue %d, Index %d, value %d\n", sMaxValue, i, gList1[i] );
        if ( sMaxValue < gList2[i] )
        {
            sTempJLIS = getJLIS( aIndex1, i ) + 1;
            //printf( " aIndex1: %d, i: %d, sTempJLIS : %d JLIS %d\n", aIndex2, i,  sTempJLIS, sJLIS );
            if ( sTempJLIS > sJLIS )
            {
                sJLIS = sTempJLIS;
                //gJLIS[aIndex1+1][aIndex2+1] = sJLIS;
                //printf ( "List 2 Set JLIS aIndex1 %d aIndex2 %d JLIS %d : i : %d\n", aIndex1, aIndex2, sJLIS, i );
            }
        }
    }
    //printf ( "JLIS aIndex1 %d aIndex2 %d JLIS %d : i : %d\n", aIndex1, aIndex2, sJLIS, i );
    gJLIS[aIndex1+1][aIndex2+1] = sJLIS;

    return sJLIS;
}

int main( void )
{
    int sCount = 0;
    int i = 0;
    int j = 0;

    scanf( "%d", &sCount );

    for ( i = 0; i < sCount; i++ )
    {
        memset( gJLIS, 0x00, sizeof(gJLIS) );

        scanf( "%d %d", &gList1Count, &gList2Count );

        /* list 1 */
        for ( j = 0; j < gList1Count; j++ )
        {
            scanf( "%d ", &gList1[j] );
        }
        
        /* list 2 */
        for ( j = 0; j < gList2Count; j++ )
        {
            scanf( "%d ", &gList2[j] );
        }
        
        printf( "%d\n", getJLIS( -1, -1 ) - 2 );
    }

    return 0;
}
