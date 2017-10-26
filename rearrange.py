import sys
import re
import random
listz = sys.argv[1:]
print(listz)
random.shuffle(listz)

def parse_dictionary(anagram_word):
    with open('/usr/share/dict/words', 'r') as f:
        pos_words = []
        dictionary = f.read().split()
        for char in  anagram_word:
            for word in dictionary:
                if word.startswith(char) and len(word) <= len(anagram_word):
                    pos_words.append(word)
                    print(word)
        print(pos_words)
            
def get_annagrams(anagram_word, rem_words):
        
        pass
if __name__ =="__main__":
    annagram_word =  input("What is the annagram word you would like to input")
    while(annagram_word.isalpha())== False:
            annagram_word = input("Enter a word that is only a string")
    parse_dictionary(annagram_word)
