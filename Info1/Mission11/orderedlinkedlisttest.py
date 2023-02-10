import unittest
from orderedlinkedlist import OrderedLinkedList, Node


class OrderedLinkedListTest(unittest.TestCase):

    def init(self):
        self.lst = OrderedLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_print(self):
        print(self.lst)


if __name__ == '__main__':
    unittest.main(verbosity=2)
