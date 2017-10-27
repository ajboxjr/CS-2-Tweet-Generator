import unittest
import vocab_game
class TestVocab(unittest.TestCase):
    def setUp(self):
        self.cheese = vocab_game.VocabCard("Cheese")
        self.water = vocab_game.VocabCard("Farts" , "The stinky shit that homeless people do")

    def test_set_definition(self):
        self.assertEqual(self.cheese.set_definition("This is a stupid thing"), self.cheese.get_definition())
    def test_get_definition(self):
        self.assertEqual(self.water.get_definition(),"The stinky shit that homeless people do")
if __name__ == '__main__':
    unittest.main()
