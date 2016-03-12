import unittest
import CANADATRIP

class Mytest(unittest.TestCase):
    def test1(self):
        trip = CANADATRIP.CanadaTrip()
        trip.insert(500, 100, 10)
        trip.insert(504, 16, 4)
        trip.insert(510,60, 6)
        self.assertEqual(trip.search(15), 480)

    def test2(self):
        trip = CANADATRIP.CanadaTrip()
        trip.insert(8030000,8030000,1)
        trip.insert(2,2,1)
        self.assertEqual(trip.search(1234567), 1234563)
        
if __name__ == "__main__":
    TS = unittest.TestSuite()
    TS.addTest(Mytest("test1"))
    TS.addTest(Mytest("test2"))
    runner = unittest.TextTestRunner()
    runner.run(TS)

