import unittest
import vocab_card
class TestFlashCards(unittest.TestCase):
    def setUp(self):
        self.spanish = vocab_card.FlashCards("Spanish Cards")
    def test_add_card(self):
        self.assertEquals(self.spanish.add_card(vocab_card.VocabCard("Hi", "A welcome"))), 
