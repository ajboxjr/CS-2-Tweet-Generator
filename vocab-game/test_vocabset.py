import unittest
from vocabset import *
from vocabcard import *

class TestVocabCard(unittest.TestCase):
    def setUp(self):
        self.spanish = VocabSet("Spanish Cards")
        self.card = VocabCard("Hola","A welcoming statement")
        self.card2 = VocabCard("Hi", "A welcome")
        self.spanish.add_card(self.card)
        self.spanish.add_card(self.card2)


    def test_add_card(self):
        
        self.assertEqual(self.spanish.add_card(VocabCard("Hi", "A welcome")), True) 
        self.assertEqual(self.spanish.add_card(VocabCard('Hola', 'Como Estas')), True)

    def test_get_card_index(self):
        self.assertEqual(self.spanish.get_card_index(1).name, 'Hi')
        self.assertEqual(self.spanish.get_card_index(100), False)

    def test_get_card(self):
        self.assertEqual(self.spanish.get_card("Hola"), self.card)
        self.assertEqual(self.spanish.get_card('sup'), False)
    def test_view_set(self):
        self.assertEqual(self.spanish.view_set(), True)
        
if __name__ == '__main__':
    unittest.main()
