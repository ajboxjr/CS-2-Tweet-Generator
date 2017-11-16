from linked_list import *
import unittest

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linkedList = LinkedList()
        self.linkedList2 = LinkedList()

    def test_append(self):
        self.assertEqual(self.linkedList.append(9), True)
        self.assertEqual(self.linkedList.append(2), True)

    def test_delete(self):
        pass

    def test_get_index(self):
        self.linkedList.append(1)
        self.linkedList.append(2)
        self.linkedList.append(3)
        self.assertEqual(self.linkedList.get_index(99), -1)
        self.assertEqual(self.linkedList2.get_index(2), 2)



if __name__ == '__main__':
    unittest.main()

