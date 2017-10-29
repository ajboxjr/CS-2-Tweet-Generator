import sys
import random

def get_pos_words(annagram_word):
    pos_word_arr = []
    annagram_set = set(annagram_word)
    print(annagram_set)
    with open('/usr/share/dict/words', 'r') as f:
        dictionary = f.read().split()
        for word in dictionary:
            if len(word) <= len(annagram_word):
                for char in annagram_word:
                    if word.startswith(char):
                        pos_word_arr.append(word)
    return pos_word_arr

def word_combinations(user_word, pos_word= None):
    compare_set = []
    for char in pos_word:
        word = set(user_word.remove(char))
        set
        compare_set.append(pos_word.(word))
    print(compare_set)
        

if __name__ == '__main__':
    input_word = sys.argv[1]
    pos_arr = get_pos_words(input_word)
    word_combination(input_word)

