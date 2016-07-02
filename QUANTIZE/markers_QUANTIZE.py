# -*- encoding=utf-8 -*-
# author : markers
'''
  Created by Markers on 2015. 12. 29.
'''

import sys
rl = lambda : sys.stdin.readline().rstrip()

def strToInt(str):
    return map(int, str)

if __name__ == "__main__":
    testCase = int(rl())
    for tc in xrange(testCase):
        #len_seq, count_of_number = rl()
        info_seq = strToInt(rl().split())
        #print len_seq, count_of_number
        print info_seq
        seq =  map(int, rl().split() )
        print seq




