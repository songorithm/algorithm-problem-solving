#!/usr/bin/python

import time
import unittest
from j2h_JaeHaSafe import JaeHaSafe

class JaeHaSafeTest(unittest.TestCase):
    input_1 = ["abbab", "babab", "ababb", "bbaba"]
    input_2 = ["RMDCMRCD","MRCDRMDC","DCMRCDRM"]

    answer_1 = 6
    answer_2 = 10

    def setUp(self):
        self.startTime = time.time()
        print

    def tearDown(self):
        print("{0}: {1}".format(self.id(), time.time() - self.startTime))

    def testShiftLeft(self):
        self.assertEquals([2,3,1], JaeHaSafe().shiftLeft([1,2,3]))

    def testShiftRight(self):
        self.assertEquals([3,1,2], JaeHaSafe().shiftRight([1,2,3]))

    def testSameWhile(self):
        self.assertEquals(1, JaeHaSafe().sameWhile([1,2,3], [3,1,2]))
        self.assertEquals(2, JaeHaSafe().sameWhile([1,2,3], [2,3,1]))

    def testSample(self):
        self.assertEquals(self.answer_1, JaeHaSafe().solve(self.input_1))
        self.assertEquals(self.answer_2, JaeHaSafe().solve(self.input_2))

if __name__ == '__main__':
    totalSuite = unittest.TestLoader().loadTestsFromTestCase(JaeHaSafeTest)
    suite = unittest.TestSuite()
#    suite.addTest(JaeHaSafeTest('testShiftLeft'))
#    suite.addTest(JaeHaSafeTest('testShiftRight'))
#o    suite.addTest(JaeHaSafeTest('testSameWhile'))
    suite.addTest(JaeHaSafeTest('testSample'))
    unittest.TextTestRunner(verbosity=2).run(suite)
#    unittest.TextTestRunner(verbosity=2).run(totalSuite)
