from vocabcard import *
from vocabset import *

class Game(object):
    def __init__(self):
        # a list of all the possible words, for checking if it's a word.
        self.dictionary = []
        # Dekcs of Vocab Cards
        self.vocab_sets = []
        self.setup()

    def upload_dict(self):
        with open('/usr/share/dict/words', 'r') as f:
            self.dictionary = f.read().split()

    def setup(self):
        self.upload_dict()

   
