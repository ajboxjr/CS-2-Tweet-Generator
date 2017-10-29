import sys
import random
class Histogram(dict):
    def __init__(self, source_text):
        self.source_text = source_text
        self.histogram()
        self.tuple = self.to_tuple()

    def unique_words(self):
        unique_arr = []
        for key , val in self.items():
            if val == 1:
                unique_arr.append(key)
        #print("Unique words: {}".format(unique_arr))
        return unique_arr

    def frequency(self, word):
        if word in self:
            print("{}: {}".format(word, self[word]))
            return self[word]
            
    def histogram(self):
        for word in self.source_text:
            if word in self: 
                self[word] += 1
            else:
                self[word] =1
        #print(self)

    def stochastic(self, tup_histogram):
        for i in range(len(tup_histogram)):
            print(tup_histogram[i][0])

    def to_tuple(self):
        tuple_histogram = []
        for key,val in self.items():
            tuple_histogram.append((key,val))
        #print(tuple_histogram)
        return tuple_histogram

    def export_histogram(self, histogram_title):
        file =  open(histogram_title+'.txt', 'w')
        for key, val in self.items():
            string = "{} {}\n".format(key,val)
            file.write(string)
        file.close()

def read_text(file_name):
    with open(file_name) as f:
       return f.read().split()

def handle_input(input_word):
    if input_word.endswith('.txt'):
        print('input a text file:' + input_word)
        source_text = read_text(input_word) 
        return source_text
    else:
        print("input raw string \n")
        return input_word

if __name__ == '__main__':

    histogramz = Histogram(source_text)
    histogramz.histogram()
    histogramz.frequency('this')
    histogramz.unique_words()
