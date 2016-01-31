# -*- encoding=utf-8 -*-
# author : markers
'''
  Created by Markers on 2016. 1. 18.
'''

import sys

rl = lambda : sys.stdin.readline()


n_length = [-1] * 51

def generate_length_nth():
    n_length[0] = 1
    for n in range(1,51):
        n_length[n] = min(1000000001, n_length[n-1]*2+2)

#def generate_length_nth():
#    n_length.append(1)
#    for n in range(1,50):
#        n_length.append(min(1000000001, n_length[n-1]*2+2))


def curve(seed, n_th, skip):
    if n_th == 0:
        #print seed,
        return seed[skip]
    for word in seed:
        if word == "X" or word == "Y":
            if skip >= n_length[n_th]:
                skip -= n_length[n_th]
            elif word == "X":
                return curve("X+YF", n_th-1, skip)
            elif word == "Y":
                return curve("FX-Y", n_th-1, skip)
        elif skip > 0:
            skip -= 1
        else:
            return word
    return


if __name__ == "__main__":
    testCase = int(rl())
    generate_length_nth()
    for tc in xrange(testCase):
        n_th, position, length = map(int, rl().rstrip().split())
        string = []
        for l in xrange(length):
            string.append( curve("FX", n_th, position-1+l ) )
        print ''.join(string)
        #print string

