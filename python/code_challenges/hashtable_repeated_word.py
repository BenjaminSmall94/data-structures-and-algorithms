from data_structures.hashtable import Hashtable
import re


def first_repeated_word(words):
    word_arr = words.split()
    for idx, word in enumerate(word_arr):
        word_arr[idx] = re.sub(r'[^a-zA-Z]', '', word).lower()
    words = Hashtable()
    for word in word_arr:
        if words.contains(word):
            return word
        words.set(word, 1)
