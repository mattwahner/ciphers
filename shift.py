
from . import letters
from collections import Counter

class ShiftCipher():
    
    def __init__(self, key):
        self.key = key

    @staticmethod
    def from_ciphertext(ciphertext):
        ciphertext_counter = Counter(ciphertext)
        most_common_letter = ciphertext_counter.most_common(1)[0][0]
        most_common_letter_assumed_as_e = ShiftCipher._shift(most_common_letter, -1 * letters.encode('E'))
        return ShiftCipher(letters.encode(most_common_letter_assumed_as_e))

    def encrypt(self, s):
        return ''.join([ShiftCipher._shift(c, self.key) for c in s])

    def decrypt(self, s):
        return ''.join([ShiftCipher._shift(c, -1 * self.key) for c in s])

    @staticmethod
    def _shift(c, amount):
        return letters.decode((letters.encode(c) + amount) % 26)
