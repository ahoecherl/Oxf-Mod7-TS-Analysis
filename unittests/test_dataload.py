import unittest
import dataload


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(dataload.add(10, 5), 15)
        self.assertEqual(dataload.add(-1, 1), 0)
        self.assertEqual(dataload.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(dataload.subtract(10, 5), 5)
        self.assertEqual(dataload.subtract(-1, 1), -2)
        self.assertEqual(dataload.subtract(-1, -1), 0)

    def test_divide(self):
        self.assertEqual(dataload.divide(10, 5), 2)
        self.assertEqual(dataload.divide(-1, 1), -1)
        self.assertEqual(dataload.divide(-1, -1), 1)


if __name__ == '__main__':
    unittest.main()
