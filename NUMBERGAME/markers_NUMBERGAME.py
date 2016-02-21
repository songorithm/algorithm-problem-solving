# -*- encoding=utf-8 -*-
# author : markers
'''
  Created by Markers on 2016. 1. 26.
'''

import sys

rl = lambda : sys.stdin.readline()

numberList = None
check_number = None


def number_game(left,right):

    result = [ -sys.maxint ] * 4

    if left > right:
        return 0

    if check_number[left][right] != None:
        return check_number[left][right]

    result[0] = (numberList[left]-number_game(left+1,right))
    result[1] = (numberList[right]-number_game(left,right-1))

    if right - left + 1 >= 2:
        result[2] = (0-number_game(left+2,right))
        result[3] = (0-number_game(left,right-2))

    check_number[left][right] = max(result)

    return check_number[left][right]



if __name__ == "__main__":
    testCase = int(rl())
    for tc in xrange(testCase):
        numberSize = int(rl())

        numberList = map(int, rl().split())

        check_number = [ [ None for x in range(numberSize) ] for x in range(
                numberSize) ]

        print number_game(0, numberSize-1)
