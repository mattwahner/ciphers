
from . import letters
from . import shift
from copy import copy
from collections import Counter

class VigenereCipher():

    def __init__(self, keyword):
        self.keyword = keyword
        self.keyword_length = len(keyword)
        self.shift_ciphers = [shift.ShiftCipher(letters.encode(c)) for c in keyword]

    def __copy__(self):
        return type(self)(self.keyword)

    @staticmethod
    def from_basic_ciphertext(ciphertext, keyword_length):
        buckets = letters.bucket(ciphertext, keyword_length)
        shift_ciphers = [shift.ShiftCipher.from_ciphertext(bucket) for bucket in buckets]
        keyword = ''.join([letters.decode(cipher.key) for cipher in shift_ciphers])
        return VigenereCipher(keyword)

    def change_shift_cipher(self, i, c):
        self.shift_ciphers[i] = shift.ShiftCipher.from_ciphertext(c)
        keyword_list = list(self.keyword)
        keyword_list[i] = letters.decode(self.shift_ciphers[i].key)
        self.keyword = ''.join(keyword_list)

    @staticmethod
    def from_ciphertext(ciphertext, keyword_length):
        cipher = VigenereCipher.from_basic_ciphertext(ciphertext, keyword_length)
        print('Basic ciphertext keyword:', cipher.keyword)
        buckets = letters.bucket(ciphertext, keyword_length)
        bucket_counters = [Counter(bucket) for bucket in buckets]
        changed = True
        while changed:
            changed = False
            for i in range(keyword_length):
                max_ic = letters.ic(cipher.decrypt(ciphertext))
                for c in [common_letter[0] for common_letter in bucket_counters[i].most_common(10)]:
                    new_cipher = copy(cipher)
                    new_cipher.change_shift_cipher(i, c)
                    new_ic = letters.ic(new_cipher.decrypt(ciphertext))
                    if new_ic > max_ic:
                        changed = True
                        print('Old cipher keyword ', cipher.keyword, ' is changing to new cipher keyword ', new_cipher.keyword)
                        cipher = new_cipher
                        max_ic = new_ic
        return cipher

    def encrypt(self, s):
        return ''.join([self.shift_ciphers[i % self.keyword_length].encrypt(c) for i, c in enumerate(s)])

    def decrypt(self, s):
        return ''.join([self.shift_ciphers[i % self.keyword_length].decrypt(c) for i, c in enumerate(s)])
