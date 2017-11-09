import random

import time
import sys

# Getting all words in the dictionary
def get_words_list(file_name):
	with open(file_name, 'r') as f:
		dictionary = f.read().split()
		return dictionary

# Subtracting start time from end time
def get_elapsed_time(start_time):
    end_time = time.time()
    print("compilation time {}".format(end_time - start_time))

# Return random X amount of random words
def get_rand_word(word_arr):
	return word_arr[random.randint(0,len(word_arr)-1)]

def random_words(word_arr,word_cnt):
	rand_words = []
	for _ in range(word_cnt):
		rand_words.append(get_rand_word(word_arr))
	return " ".join(rand_words)

if __name__ == '__main__':

	#Benchmarking: creating start time
    start_time = time.time()
    dictionary_arr = get_words_list(sys.argv[1])
    random_words(dictionary_arr, int(sys.argv[2]))
    get_elapsed_time(start_time)
