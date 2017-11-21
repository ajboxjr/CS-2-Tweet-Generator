import random
import time
import sys
"""
Get random words from the system's Dictionary.
This program imlements the skills:
    - I/O
    - Benchmarking
    - Random Library
"""
def get_words_list(file_name):
    """ Getting all words in the dictionary """
	with open(file_name, 'r') as f:
		dictionary = f.read().split()
		return dictionary

def get_elapsed_time(start_time):
    """Benchmarking project, by start and end time"""
    end_time = time.time()
    print("compilation time {}".format(end_time - start_time))

# Return random X amount of random words
def get_rand_word(word_arr):
	return word_arr[random.randint(0,len(word_arr)-1)]

def random_words(word_arr,word_cnt):
    """Return a string of random words size word_cnt"""
	rand_words = []
	for _ in range(word_cnt):
		rand_words.append(get_rand_word(word_arr))
	return " ".join(rand_words)

if __name__ == '__main__':

	#Benchmarking: creating start time
    start_time = time.time()
    # DIctionary words
    # /usr/share/dict/words
    dictionary_arr = get_words_list('/usr/share/dict/words')
    words = random_words(dictionary_arr, int(sys.argv[1]))
    print(words)
    get_elapsed_time(start_time)
