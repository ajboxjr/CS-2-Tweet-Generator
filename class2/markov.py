from __future__ import division, print_function  # Python 2 and 3 compatibility
from nltk.tokenize import sent_tokenize
from dictogram import *
class Markov(dict):
    """Markov is a dictionary of key(current word), val/next_word(dictogram). Takes a string of text"""
    def __init__(self, text=None):
        #Create start and stop dictogram to store the begging of words and end of words
        self['START'] = Dictogram()
        if text:
            #Creating a markov model for each sentence
            self.markov(text)
    def tokenize_sentence(self, text):
        """ Using nltk split corpus based on sentences"""
        sentence_arr = sent_tokenize(text)
        print("There are {} sentences".format(len(sentence_arr)))
        return sentence_arr

    def markov(self,text):
        """ Create a markoff model based on the text array input into the file """
        corpus = self.tokenize_sentence(text)
        print(corpus)
        x = 0
        for sentence in corpus:
            sentence = sentence.split()
            x = 0
            self['START'].add_count(sentence[0])
            # From the first to the to last word
            while x< len(sentence)-1:
                word = sentence[x]
                next_word = sentence[x+1]
                if word not in self.keys():
                    self[word]= Dictogram()
                self[word].add_count(next_word)
                x+=1
            # Adding a stop token to the final word
            self[sentence[-1]] = Dictogram()
            self[sentence[-1]].add_count('STOP')

        def weight_markov(self):
            """ Return a key with a value of possible next words weighte """
            markov_weight = {}
            for key, val in self.items():
                markov_weight[key] = val.weighted_hist()
            return markov_weight

        def generate_sentence(self, length=10):
            """Return a sentence based on markof model""" 
            sentence = ""
            weights = self.weight_markov()
            #Get First word

def main():
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())
        marky = Markov("one fish two fish red fish blue fish. Dr. Suess should be proud that i can use his stuff.")
        print(marky)
        weighted_markov = marky.weight_markov()
        marky.generate_sentence()
main()
