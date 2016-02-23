import time
import unittest
from j2h_StrJoin import StrJoin

class StrJoinTest(unittest.TestCase):
    def defaultSort(self, l):
        l.sort()
        return l

    def mySort(self, l):
        newValue = l.pop()
        for idx in xrange(len(l)):
            if l[idx] > newValue:
                l.insert(idx, newValue)
                return l
        l.append(newValue)
        return l

    def myImproveSort(self, l):
        newValue = l.pop()
        start = 0
        end = len(l) - 1

        while True:
            if start == end:
                if l[start] > newValue:
                    l.insert(start, newValue)
                    break
                else:
                    l.insert(start+1, newValue)
                    break
            if start > end:
                l.insert(start, newValue)

            mid = (start+end)/2
            if l[mid] < newValue:
                start = mid + 1
            elif l[mid] > newValue:
                end = mid + 1
            else:
                l.insert(mid, newValue)
                break

        return l

    def setUp(self):
        self.startTime = time.time()
        print

    def tearDown(self):
        print("{0}: {1}".format(self.id(),
                                (time.time() - self.startTime)*10000)) # * 10000

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

    def testSolveWithCustomMethod(self):
        self.assertEquals(3222, StrJoin().calCostWithSortMethod(
            [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,
             1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,
             1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,
             1,1,1,1,1,1,1,1,2], self.mySort))

    def testSolveWithCustomImproveMethod(self):
        self.assertEquals(3222, StrJoin().calCostWithSortMethod(
            [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,
             1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,
             1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,
             1,1,1,1,1,1,1,1,2], self.myImproveSort))


    def testSolveWithCustomDefaultMethod(self):
        self.assertEquals(3222, StrJoin().calCostWithSortMethod(
            [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,
             1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,
             1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,
             1,1,1,1,1,1,1,1,2], self.defaultSort))

    def testSolveWithDefaultSort(self):
        self.assertEquals(3222, StrJoin().calCost(
            [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,
             1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,
             1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,
             1,1,1,1,1,1,1,1,2]))


if __name__ == '__main__':
#    suite = unittest.TestLoader().loadTestsFromTestCase(StrJoinTest)
    suite = unittest.TestSuite()
#    suite.addTest(StrJoinTest('testSolve3'))
    suite.addTest(StrJoinTest('testSolveWithCustomMethod'))
    suite.addTest(StrJoinTest('testSolveWithCustomImproveMethod'))
    suite.addTest(StrJoinTest('testSolveWithCustomDefaultMethod'))
    suite.addTest(StrJoinTest('testSolveWithDefaultSort'))
    unittest.TextTestRunner(verbosity=2).run(suite)
