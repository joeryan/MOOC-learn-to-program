import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_less_than_1_bus(self):
        expect_buses = 1
        buses = a1.num_buses(49)
        self.assertEqual(expect_buses, buses)

    def test_exactly1_bus(self):
        expect_buses = 1
        buses = a1.num_buses(50)
        self.assertEqual(expect_buses, buses)

    def test_more_than1_bus(self):
        expect_buses = 2
        buses = a1.num_buses(99)
        self.assertEqual(expect_buses, buses)

    

if __name__ == '__main__':
    unittest.main(exit=False)
