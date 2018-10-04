
from collections import Counter


def encode(c):
    return ord(c.upper()) - ord('A')


def decode(c):
    return chr(c + ord('A'))


def ic(text):
    num_letters = len(text)
    if num_letters <= 1:
        return 0
    text_counter = Counter(text)
    return sum([v * (v - 1) for _, v in text_counter.items()]) / ((num_letters - 1) * num_letters)


def bucket(text, buckets):
    return [text[i::buckets] for i in range(buckets)]


def average_ic(buckets):
    return sum(map(ic, buckets)) / len(buckets)


def guess_keyword_length(ciphertext, max_bucket):
    for i in range(1, max_bucket + 1):
        print(i, average_ic(bucket(ciphertext, i)))
