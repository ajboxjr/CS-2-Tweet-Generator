import unittest
from histogram import *

class TestSchoasticSampling(unittest.TestCase):
    def setUp(self):
        self.sample1 = histogram("This is the text that i will put in the histogram".split())
    def test_unique_word(self):
        self.assertEqual(unique_words(self.newsample1), "hello") 
if __name__ == "__main__":
    unittest.main()
