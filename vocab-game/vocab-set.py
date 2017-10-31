from vocabcard import *

class VocabSet(object):
    def __init__(self, title):
        self.title = title
        self.cards = []

    def add_card(self, card):
        if not get_card(card.name):
            self.cards(new_card)
            print("Added Card Sucessfully")
            return True
        else:
            print("Can't add this card, it currently has no definition")
            return False
#   Infput a card name or descroption and return a card object
    def get_card(self, card_info):
        for card in self.cards:
            if card_info == card.name:
                return card
            elif card_info == card.description:
                return card
            else:
                return False 

    def remove_card(self, card_info):
        for index in range(len(self.cards)):
            if card_info == self.cards[index].name:
                self.cards[index].pop(index)
            elif card_info == self.cards[index].description:
                self.cards.pop(index)


