import unittest
Brackets2 = __import__('free-lunch_BRACKETS2')

class Mytest(unittest.TestCase):
    def test1(self):
        bracket = Brackets2.Brackets2("()()")
        self.assertEqual(bracket.isValidated(), True)

    def test2(self):
        bracket = Brackets2.Brackets2("({[}])")
        self.assertEqual(bracket.isValidated(), False)

    def test3(self):
        bracket = Brackets2.Brackets2("({}[(){}])")
        self.assertEqual(bracket.isValidated(), True)

    def test4(self):
        bracket = Brackets2.Brackets2("(((((")
        self.assertEqual(bracket.isValidated(), False)

    def test5(self):
        bracket = Brackets2.Brackets2("]]]]]")
        self.assertEqual(bracket.isValidated(), False)


if __name__ == "__main__":
    TS = unittest.TestSuite()
    TS.addTest(Mytest("test1"))
    TS.addTest(Mytest("test2"))
    TS.addTest(Mytest("test3"))
    TS.addTest(Mytest("test4"))
    TS.addTest(Mytest("test5"))
    runner = unittest.TextTestRunner()
    runner.run(TS)

