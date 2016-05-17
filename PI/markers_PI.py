# -*- encoding=utf-8 -*-
# author : markers
'''
  Created by Markers on 2015. 12. 27.
'''
import sys
rl = lambda : sys.stdin.readline()


def strToInt(str):
    return map(int, str)

def check(pi):
    #case 1
    # 모든 숫자가 같을 때 1점
    if all( x == pi[0] for x in pi ):
        return 1
    #case 2
    #숫자가 1씩 단조 증가하거나 단조 감소할때 2점
    elif all( x-y == 1 for x, y in zip( pi, pi[1:] ) ) or all( x-y == -1 for x, y in zip( pi, pi[1:] )):
        return 2
    #case 3
    # 두 개의 숫자가 번갈아가며 나타날 때 4점
    elif ( pi[0:] != pi[1:] ) and all( x == pi[0] for x in pi[::2] ) and all( x == pi[1] for x in pi[1::2]):
        return 4
    #case 4
    # 숫자가 등차 수열을 이룰 때 5점
    elif all( x-y == y-z for x, y, z in zip( pi, pi[1:], pi[2:] ) ):
        return 5
    #case 5
    # 그 의외의 모든 경우 10점
    return 10

def judge(pi):

    result = 0

    for index in xrange(len(pi)):

        if index < 2:
            continue
        if index <= 4:
            memoization[index] = check(pi[0:index+1])
        if index - 3 >= 2:
            temp = memoization[index-3] + check(pi[index-2:index])
            memoization[index] = temp if memoization[index] == None or temp < memoization[index] else memoization[index]
        if index - 4 >= 2:
            temp = memoization[index-4] + check(pi[index-3:index])
            #memoization[index] = temp if temp > memoization[index] else memoization[index]
            memoization[index] = temp if memoization[index] == None or temp < memoization[index] else memoization[index]
        if index - 5 >= 2:
            temp = memoization[index-5] + check(pi[index-4:index])
            memoization[index] = temp if memoization[index] == None or temp < memoization[index] else memoization[index]

        result = memoization[index]

    return result

if __name__ == "__main__":
    testcase = int(rl())
    for tc in xrange(testcase):
        pi = rl().rstrip()
        pi = strToInt(pi)
        global memoization
        memoization = [None] * len(pi)
        #print memoization
        print judge(pi)
