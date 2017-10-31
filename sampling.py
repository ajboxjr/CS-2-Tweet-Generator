import sys
import random
from histogram import *

            

def stochastic_sample(histogram):
    return histogram.tuple[random.randint(0,len(histogram.tuple)-1)][0]

def probablity(sample):
    total_words = sum([int(item[1]) for item in sample])
    rand_pop = {} 
    for hist in sample:
        print("{} : {}".format(hist[0], round(int(hist[1])/total_words,5)))

if __name__ =="__main__":
    text = handle_input('text.txt')
    histogram = Histogram(text)
    print(histogram.tuple)
    print(histogram.frequency("this"))
    print(stochastic_sample(histogram.tuple))
    probablity(histogram.tuple)
    print(histogram.sort('word'))
    print(histogram.sort('count'))

