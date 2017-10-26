import random
import sys
def random_words(word_cnt):
    with open('/usr/share/dict/words', 'r') as f:
        dictionary = f.read().split()
        for _ in range(word_cnt):
            print(random.choice(dictionary))
if __name__ == '__main__':
    random_words(int(sys.argv[1]))
