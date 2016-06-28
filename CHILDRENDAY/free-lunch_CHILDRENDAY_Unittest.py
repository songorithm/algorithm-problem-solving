test = __import__('free-lunch_CHILDRENDAY')
import unittest

class Test_CHILDRENDAY(unittest.TestCase):
    def test_append_1(self):
        # Case : result < Mod
        self.assertEqual(test.append(0, 3, 9), 3)

    def test_append_2(self):
        # Case : result < Mod
        self.assertEqual(test.append(0, 5, 9), 5)

    def test_append_3(self):
        # Case : result >= Mod
        self.assertEqual(test.append(5, 3, 9), 8 + 9)

    def test_solve_1(self):
        self.assertEqual(test.solve((1,),7,0), '111111')

    def test_solve_2(self):
        self.assertEqual(test.solve((1,),10,1), '11')

    def test_solve_3(self):
        self.assertEqual(test.solve((0,),7,3), 'IMPOSSIBLE')

    def test_solve_4(self):
        self.assertEqual(test.solve((3,4,5),9997, 3333), '35355353545')

    def test_solve_5(self):
        self.assertEqual(test.solve((3,5), 9, 8), '35')



if __name__ == "__main__":
    unittest.main()
