# -*- encoding=utf-8 -*-
# author : markers
'''
  Created by Markers on 2016. 2. 22.
'''

import sys
from operator import itemgetter

rl = lambda : sys.stdin.readline().rstrip()

def check_time(lunchbox_time):

    time = 0
    warm_time = 0
    for box in lunchbox_time:
        warm_time += box[0]
        time = max(time, warm_time + box[1])
    return time


if __name__ == "__main__":
    testCase = int(rl())
    for tc in xrange(testCase):
        num_box = int(rl())
        box_warm_time = map(int, rl().split())
        box_eat_time = map(int, rl().split())
        lunchbox_time = zip(box_warm_time, box_eat_time)
        lunchbox_time = sorted(lunchbox_time, key=itemgetter(1),reverse=True)
        #print lunchbox_time
        print check_time(lunchbox_time)
