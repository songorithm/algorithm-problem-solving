# -*- encoding=utf-8 -*-
# author : markers
'''
  Created by Markers on 2016. 2. 28.
'''

import sys
from _collections import defaultdict
from collections import OrderedDict

rl = lambda: sys.stdin.readline()


class Allergy():
    best = 987654321

    def __init__(self):
        self.dictionary = defaultdict(list)
        self.eater = {}

    def clear(self):
        self.dictionary.clear()
        self.eater.clear()
        self.best = 987654321

    def start(self):
        testCase = int(rl())
        for tc in xrange(testCase):
            people_num, food_num = map(int, rl().strip().split())
            people = rl().strip().split()
            for food_index in xrange(food_num):
                can_eat_people = rl().split()
                # print can_eat_people[1:]
                self.set_food_list(food_index, can_eat_people[1:])
            self.dictionary = OrderedDict(
                sorted(self.dictionary.items(), key=lambda
                    x:
                len(x[1])))

            self.check(0)
            print self.best
            self.clear()

    def set_food_list(self, food_idx, people):
        for person in people:
            self.dictionary.setdefault(person, []).append(food_idx)

    def check(self, cnt):
        # 가지치기
        # print "cnt = {} , best = {}".format(cnt,self.best)
        if cnt >= self.best: return

        # 모든 사람들이 다 먹었다면 종료
        if not bool(self.dictionary):
            self.best = cnt
            return

        key = next(self.dictionary.iterkeys())
        # print "key =  {} ".format(key)
        # print key
        # print self.dictionary[key]

        # 먹은 음식 체크
        for food_idx in self.dictionary[key]:
            back = OrderedDict([(key, values) for key, values in
                                self.dictionary.items() if food_idx in values])
            for key in back.keys():
                self.dictionary.pop(key)
            cnt += 1
            self.check(cnt)
            cnt -= 1
            self.dictionary.update(back)


if __name__ == "__main__":
    # import cProfile
    allergy = Allergy()
    allergy.start()
    # cProfile.run('print allergy.start(); print')