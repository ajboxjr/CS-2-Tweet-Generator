import sys
from itertools import permutations
import random

class Annagram(object):
    def __init__(self,word):
        self.word = None
        if word:
            self.word = word
            self.get_pos_words()

    def set_word(self,word):
        """Set Annagram Word"""
        self.word = word
    def has_word(self):
        """Check if class has a word for annagrams"""
        return self.word != None
    

    def get_pos_words(self):
        pos_word_arr = []
        annagram_set = set(self.word)
        for word in get_dictionary():
            if len(word) <= len(self.word):
                for char in annagram_set:
                    if word.startswith(char):
                        pos_word_arr.append(word)
        return pos_word_arr

            
    def word_permutation(self):
        pos_words = self.get_pos_words()
        print(pos_words)
        for length in range(1,len(self.word)+1):
            perms = set(map("".join, permutations(self.word, length)))
            for word in perms:
                if word in pos_words:
                    print(word)

def get_dictionary():
    with open('/usr/share/dict/words', 'r') as f:
        dictionary = f.read().split()
    return dictionary

if __name__ == '__main__':
    input_word = sys.argv[1]
    pos_arr = Annagram(input_word)
    pos_arr.word_permutation()

