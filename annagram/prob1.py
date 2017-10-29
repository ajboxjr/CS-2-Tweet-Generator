import random
import datetime
import time
import sys

def get_elapsed_time(start_time):
    end_time = time.time()
    print("compilation time {}".format(end_time - start_time))


def random_words(word_cnt):
    with open('/usr/share/dict/words', 'r') as f:
        dictionary = f.read().split()
        for _ in range(word_cnt):
            print(dictionary[random.randint(0,len(dictionary)-1)], end= " ")
if __name__ == '__main__':
    start_time = time.time()
    random_words(int(sys.argv[1]))
    get_elapsed_time(start_time)
