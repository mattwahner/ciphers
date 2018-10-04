
import unittest
from .. import vigenere

class TestVigenereCipher(unittest.TestCase):

    def test_instance(self):
        vigenere_instance = vigenere.VigenereCipher('KEY')
        self.assertEqual(vigenere_instance.keyword, 'KEY')
        self.assertEqual(vigenere_instance.keyword_length, 3)
        self.assertEqual(vigenere_instance.shift_ciphers[0].key, 10)
        self.assertEqual(vigenere_instance.shift_ciphers[1].key, 4)
        self.assertEqual(vigenere_instance.shift_ciphers[2].key, 24)

    def test_encrypt(self):
        vigenere_instance = vigenere.VigenereCipher('KEY')
        self.assertEqual(vigenere_instance.encrypt('ATTACKZ'), 'KXRKGIJ')

    def test_decrypt(self):
        vigenere_instance = vigenere.VigenereCipher('KEY')
        self.assertEqual(vigenere_instance.decrypt('KXRKGIJ'), 'ATTACKZ')

    def test_from_basic_ciphertext(self):
        vigenere_instance = vigenere.VigenereCipher.from_basic_ciphertext('EEEE', 2)
        self.assertEqual(vigenere_instance.keyword, 'AA')

    def test_change_shift_cipher(self):
        vigenere_instance = vigenere.VigenereCipher('KEY')
        vigenere_instance.change_shift_cipher(1, 'E')
        self.assertEqual(vigenere_instance.keyword, 'KAY')

if __name__ == '__main__':
    unittest.main()
