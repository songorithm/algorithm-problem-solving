# -*- encoding=utf-8 -*-
# author : markers
'''
  Created by Markers on 2016. 3. 20.
'''

from __future__ import division
import sys
import math

rl = lambda : sys.stdin.readline()

class Ratio:

    def __init__(self, num_game, win):
        self.num_game = num_game
        self.win = win
        self.ratio = int(self.win * 100 / self.num_game)   # int로 변환하면 통과.
        # 이유가?
        self.low = 0
        self.high = 1000000000

    def bisection(self):
        """
        이분법
        :return:
        """
        if self.ratio >= 99.0:
            return -1

        while self.low + 1 < self.high:
            self.mid = (self.low+self.high)/2
            if self.ratio+1 >= (self.win+self.mid)*100/(
                        self.num_game+self.mid):
                self.low = self.mid
            else:
                self.high = self.mid

        return round(self.high)


    def calculate(self):
        """
        This method is to find ratio number
        X >= N^2 / (99N-100M)
        N is num of game
        M is win game

        :return:
        X
        """

        result = 0
        # 기저 사례 검사   -1
        # 20억이 넘는 게임을 하면 포기.
        if self.ratio >= 99.0:
            return -1


        # result = self.num_game / float( 99 - self.ratio )

        result = math.ceil((100*self.win-(self.ratio+1)*self.num_game)/(self.ratio-99))
        # 계산
        # result = self.num_game**2 / ( 99 * self.num_game - 100 * self.win)
        # print "num_game : {} , win_game : {}".format(self.num_game, self.win)
        # print "ration : {} ".format(self.ratio)

        if result >= 2000000000:
            return -1

        return result



import unittest

class TestRatio(unittest.TestCase):

    def test_calculate(self):
        self.assertEqual(1,Ratio(10,8).calculate())
        self.assertEqual(6,Ratio(100,80).calculate())
        self.assertEqual(-1,Ratio(47,47).calculate())
        self.assertEqual(1000,Ratio(99000,0).calculate())
        self.assertEqual(19230770,Ratio(1000000000,470000000).calculate())
        self.assertEqual(-1,Ratio(100,99).calculate())
        self.assertEqual(10101011,Ratio(1000000000,0).calculate())

    def test_bisection(self):
        self.assertEqual(1,Ratio(10,8).bisection())
        self.assertEqual(6,Ratio(100,80).bisection())
        self.assertEqual(-1,Ratio(47,47).bisection())
        self.assertEqual(1000,Ratio(99000,0).bisection())
        self.assertEqual(19230770,Ratio(1000000000,470000000).bisection())
        self.assertEqual(-1,Ratio(100,99).bisection())
        self.assertEqual(10101011,Ratio(1000000000,0).bisection())



if __name__ == "__main__":
    for tc in xrange(int(rl())):
        num_game, win = map(float, rl().rstrip().split())
        # print int(Ratio(num_game, win).calculate())
        print int(Ratio(num_game, win).bisection())



    # unit test
    # suite = unittest.TestSuite()
    # suite.addTest(TestRatio.test_calculate())
    # suite.addTest(TestRatio.test_bisection())

    # suite = unittest.TestLoader().loadTestsFromTestCase(TestRatio)
    # unittest.TextTestRunner(verbosity=2).run(suite)
