import time
import unittest
from StrJoin import StrJoin

class StrJoinTest(unittest.TestCase):
    def mySort(self, l):
        newValue = l.pop()
        for idx in xrange(len(l)):
            if l[idx] > newValue:
                return l[:idx] + [newValue] + l[idx:]
        return l + [newValue]

    def setUp(self):
        self.startTime = time.time()
        print

    def tearDown(self):
        print("{0}: {1}".format(self.id(), (time.time() - self.startTime)*10000))

    def testSolve(self):
       self.assertEquals(12, StrJoin().calCost([2,4,2]))

    def testSolve2(self):
        self.assertEquals(12, StrJoin().calCostWithSortMethod([2,4,2], sorted))

    def testSolve3(self):
        self.assertEquals(12, StrJoin().calCostWithSortMethod([2,4,2], self.mySort))

    def testSolve4(self):
        self.assertEquals(26, StrJoin().calCostWithSortMethod([3,1,3,4,1], self.mySort))

    def testSolve5(self):
        self.assertEquals(27, StrJoin().calCostWithSortMethod([1,1,1,1,1,1,1,2], self.mySort))

    def testSolve6(self):
        self.assertEquals(27, StrJoin().calCost([1,1,1,1,1,1,1,2]))

    def testSolve7(self):
        self.assertEquals(1087, StrJoin().calCostWithSortMethod([1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,
1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,
1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,
1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2], self.mySort))

    def testSolve8(self):
        self.assertEquals(1087, StrJoin().calCost([1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,
1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,
1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,
1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2]))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(StrJoinTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
