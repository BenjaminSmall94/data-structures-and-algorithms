from data_structures.hashtable import Hashtable


def left_join(synonyms, antonyms):
    joined_list = []
    for word in synonyms:
        if word in antonyms:
            joined_list.append([word, synonyms[word], antonyms[word]])
        else:
            joined_list.append([word, synonyms[word], "NONE"])
    return joined_list
