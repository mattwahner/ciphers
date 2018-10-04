
import unittest
from .. import shift

class TestShiftCipher(unittest.TestCase):

    def test_instance(self):
        shift_instance = shift.ShiftCipher(3)
        self.assertEqual(shift_instance.key, 3)

    def test_encrypt(self):
        shift_instance = shift.ShiftCipher(3)
        self.assertEqual(shift_instance.encrypt('ATESTZ'), 'DWHVWC')

    def test_decrypt(self):
        shift_instance = shift.ShiftCipher(3)
        self.assertEqual(shift_instance.decrypt('DWHVWC'), 'ATESTZ')

    def test_from_ciphertext(self):
        shift_instance = shift.ShiftCipher.from_ciphertext('EEEEE')
        self.assertEqual(shift_instance.key, 0)
        self.assertEqual(shift_instance.encrypt('A'), 'A')

if __name__ == '__main__':
    unittest.main()
