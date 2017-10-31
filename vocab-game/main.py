from vocabcard import *
from vocabset import *

dictionary = [] 
vocab_sets = [] 

class Game(object):
    def __init__(self):
        self.vocab_sets = []
        self. dictionary = [] 
    
    def get_dictionary(self):
        with open('/usr/share/dict/words', 'r') as f:
            self.dictionary = f.read().split()

    def get_set(self, deck_name):
        for deck in self.vocab_sets:
            if deck.title == deck_name:
                return deck
        return None

    def new_set(self, set_name):
        self.vocab_sets.append(VocabSet(set_name))
        print("Sucessfuly added {}".format(set_name))

    def view_sets(self):
        for deck in self.vocab_sets:
            print(deck.title)
        
    def mainloop(self):
        option = None
        while option != 'q':
            option = int(input("Which option would you like"))
            if option ==1:
                title = input("What would you like name this?")
                game.new_set(title)
            if option == 2:
                game.view_sets()
                deck = game.get_set(input("Which set"))
                card_amt = int(input("How many cards would you like to add"))
                for _ in range(card_amt):
                    name = input("What would you like to name this deck")
                    definition = input("{}. Definition: ".format(name))
                    card = VocabCard(name, definition)
                    deck.add_card(card)
                    print("sucessfully added {}".format(card.name))

if __name__ == '__main__':
        game = Game()
        game.mainloop()

