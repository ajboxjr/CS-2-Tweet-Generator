from vocabcard import *

class VocabSet(object):
    def __init__(self, title):
        self.title = title
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)
        return True
    def remove_card(self, card):
        del self.cards[get_card(card)]

#   Input a card name or descroption and return a card object
    def get_card_index(self, index):
        try:
            return self.cards[index]
        except IndexError:
            print("Sorry, enter another number")
            return False

    def get_card(self, card_info):
        for card in self.cards:
            if card_info == card.name:
                return card
            elif card_info == card.definition:
                return card
            else:
                return False 

    def remove_card(self, card_info):
        for index in range(len(self.cards)):
            if card_info == self.cards[index].name:
                del self.cards[index]
            elif card_info == self.cards[index].description:
                del self.cards[index]
    def view_set(self):
        for num, word in enumerate(self.cards):
            print("{}.{}: {}".format(num , word, word.definition))



