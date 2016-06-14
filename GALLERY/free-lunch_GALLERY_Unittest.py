test = __import__('free-lunch_GALLERY')
import unittest

class Test_GALLERY(unittest.TestCase):
    def test_exam1(self):
        connected = [[0, 1], [1, 2], [1, 3], [2, 5], [0, 4]]
        G,H = 6,5
        self.assertEqual(test.solve(G,H,connected),  3)


    def test_exam2(self):
        connected = [[0, 1], [2, 3]]
        G,H = 4,2
        self.assertEqual(test.solve(G,H,connected),  2 )

    def test_exam3(self):
        connected = [[0, 1]]
        G,H = 1000,1
        self.assertEqual(test.solve(G,H,connected),  999 )


if __name__ == "__main__":
    unittest.main()
