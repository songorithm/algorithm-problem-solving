
# -*- encoding=utf-8 -*-
# author : markers
'''
  Created by Markers on 2016. 2. 10.
'''

import sys

rl = lambda : sys.stdin.readline().rstrip()

def max_sushi_score(money, sushi_menu_count):
    # 되돌아가는 조건을 우째야되지...? 0이 되어야??
    if money is 0:
        return 0
    sushi_score = []
    for key in sushi_menu.keys():
        # 여기서 아마 시간이 많이..
        sushi_menu_count[key] += 1
        sushi_score.append(max_sushi_score(money-sushi[key], sushi_menu_count))
        sushi_menu_count[key] -= 1

    score = max(sushi_score)




if __name__ == "__main__":
    testCase = int(rl())
    for tc in xrange(testCase):
        kind_num, money = map(int, rl().split())
        global sushi_menu
        sushi_menu = dict()
        sushi_menu_count = dict()
        for _ in xrange(kind_num):
            price, score = map(int, rl().split())
            sushi_menu[price] = score
        # for sushi in sushi_menu:
        #     print sushi

        sushi_menu.clear()
        #print "**********"
