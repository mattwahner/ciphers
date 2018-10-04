
import unittest
from .. import letters

class TestLetters(unittest.TestCase):

    def test_A(self):
        self.assertEqual(letters.encode('A'), 0)
        self.assertEqual(letters.decode(0), 'A')

    def test_Z(self):
        self.assertEqual(letters.encode('Z'), 25)
        self.assertEqual(letters.decode(25), 'Z')

    def test_zero_ic(self):
        self.assertEqual(letters.ic(''), 0)
        self.assertEqual(letters.ic('A'), 0)

    def test_one_ic(self):
        self.assertEqual(letters.ic('AA'), 1)

    def test_many_ic(self):
        self.assertAlmostEqual(letters.ic('AAAAABBBBCCCDDE'), 0.19048, places=5)

    def test_bucket(self):
        self.assertEqual(letters.bucket('TEST', 3), ['TT', 'E', 'S'])

    def test_average_ic(self):
        self.assertAlmostEqual(letters.average_ic(letters.bucket('TEST', 3)), 0.33333, places=5)
        
if __name__ == '__main__':
    unittest.main()
