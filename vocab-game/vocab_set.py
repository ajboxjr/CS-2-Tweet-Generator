class VocabSet(object):
    def __init__(self, title):
        self.title = title
        self.cards = []

    def add_card(card):
        if card.has_definition():
            self.cards.append(card)
            print("Added Card Sucessfully")
        else:
            print("Can't add this card, it currently has no definition")
