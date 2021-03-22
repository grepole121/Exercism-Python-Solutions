import re
from collections import defaultdict


def count_words(sentence):
    sentence = sentence.lower()

    words = re.findall(r'[a-z0-9\']+', sentence)

    word_counts = defaultdict(int)
    for word in words:
        word_counts[(word).strip("'")] += 1

    return word_counts
