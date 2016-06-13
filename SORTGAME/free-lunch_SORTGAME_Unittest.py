test = __import__('free-lunch_SORTGAME')
import unittest

class Test_SORTGAME(unittest.TestCase):
    def test_exam1(self):
        input = [1, 2, 3, 4, 8, 7, 6, 5]
        self.assertEqual(test.solve(input),  1 )


    def test_exam2(self):
        input = [3, 4, 1, 2]
        self.assertEqual(test.solve(input),  2 )

    def test_exam3(self):
        input = [1, 2, 3]
        self.assertEqual(test.solve(input),  0 )


if __name__ == "__main__":
    unittest.main()
