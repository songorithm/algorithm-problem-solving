#!/usr/bin/python

import time
import unittest
from j2h_Potion import Potion

class PotionTest(unittest.TestCase):
    n_1 = [4, 6, 2, 4]
    p_1 = [6, 4, 2, 4]
    n_2 = [4, 6, 2, 4]
    p_2 = [7, 4, 2, 4]
    n_3 = [4, 5, 6]
    p_3 = [1, 2, 3]

    answer_1 = [0, 5, 1, 2]
    answer_2 = [1, 8, 2, 4]
    answer_3 = [3, 3, 3]

    def setUp(self):
        self.startTime = time.time()
        print

    def tearDown(self):
        print("{0}: {1}".format(self.id(), time.time() - self.startTime))

    def testCase1(self):
        self.assertEquals(self.answer_1, Potion().doSolve(self.n_1, self.p_1))

    def testCase2(self):
        self.assertEquals(self.answer_2, Potion().doSolve(self.n_2, self.p_2))

    def testCase3(self):
        self.assertEquals(self.answer_3, Potion().doSolve(self.n_3, self.p_3))

    def testGetMinRatio(self):
        self.assertEquals([1,1,2], Potion().getMinRatio([2,2,4]))
        self.assertEquals([1,2,3], Potion().getMinRatio([10,20,30]))
        self.assertEquals([2,1,4], Potion().getMinRatio([2,1,4]))
        self.assertEquals([2,3,1,2], Potion().getMinRatio([4,6,2,4]))
        self.assertEquals([4,5,6], Potion().getMinRatio([4,5,6]))


    def testGetGCD(self):
        self.assertEquals(3, Potion().getGCD([3,6]))
        self.assertEquals(3, Potion().getGCD([3,6,9]))
        self.assertEquals(5, Potion().getGCD([10,15,20,30,25]))
        self.assertNotEquals(5, Potion().getGCD([10,13]))
        self.assertNotEquals(2, Potion().getGCD([10,13,5]))

if __name__ == '__main__':
    totalSuite = unittest.TestLoader().loadTestsFromTestCase(PotionTest)
    suite = unittest.TestSuite()
    suite.addTest(PotionTest('testGetGCD'))
    suite.addTest(PotionTest('testGetMinRatio'))
    suite.addTest(PotionTest('testCase1'))
    suite.addTest(PotionTest('testCase2'))
    suite.addTest(PotionTest('testCase3'))
    unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.TextTestRunner(verbosity=2).run(totalSuite)
    
