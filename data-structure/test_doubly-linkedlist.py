from doubly_linkedlist import *
import unittest

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        d1 = DoublyLinkedList()
        d2 = DoublyLinkedList(2)

    def test_append(self):
        self.assertEqual(d1.append(

