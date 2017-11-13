import sys
import random
from histogram import *

            

def stochastic_sampling(weighted_hist):
    rand_percent = random.uniform(0,1)
    cum_weight = 0
    for token in weighted_hist:
        cum_weight += word[1]
        if cum_weight > rand_percent:
            return word[0]

def weighted_hist(sample):
    weight_arr = []
    total_words = sum([int(item[1]) for item in sample])
    for hist in sample:
        weight_arr.append([hist[0], hist[1]/total_words])
    return weight_arr

def cum_weight_hist(histogram):
    cumlative_arr = []
    total_words = sum([int(item[1]) for item in sample])
    for word in histogram:
        pass

def population(histogram, pop_size):
    pop_dict = {}
    for _ in range(pop_size):
        word = stochastic_sampling(histogram)
        if word in pop_dict:
            pop_dict[word] +=1
        else:
            pop_dict[word] = 1
    return pop_dict.keys()

if __name__ =="__main__":
    text = handle_input(sys.argv[1])
    histogram = Histogram(text)
    text = handle_input(sys.argv[1])
    print(histogram.frequency("this"))
    print(histogram.sort('word'))
    print(histogram.sort('count'))
    weighted_arr = weighted_hist(histogram.tuple)
    print(population(weighted_arr, 4))
