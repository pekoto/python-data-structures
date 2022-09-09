import unittest

from doubly_linked_list import DoublyLinkedList


class DoublyLinkedListTest(unittest.TestCase):

    def test_add_left(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.add_left(1)
        doubly_linked_list.add_left(2)
        doubly_linked_list.add_left(3)

        self.assertEqual(3, doubly_linked_list.size)
        self.assertEqual(3, doubly_linked_list._head.val)
        self.assertEqual(2, doubly_linked_list._head.next.val)
        self.assertEqual(1, doubly_linked_list._head.next.next.val)

    def test_add_right(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.add_right(1)
        doubly_linked_list.add_right(2)
        doubly_linked_list.add_right(3)

        self.assertEqual(3, doubly_linked_list.size)
        self.assertEqual(1, doubly_linked_list._head.val)
        self.assertEqual(2, doubly_linked_list._head.next.val)
        self.assertEqual(3, doubly_linked_list._head.next.next.val)

    def test_pop_left(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.add_left(1)
        doubly_linked_list.add_left(2)
        doubly_linked_list.add_left(3)

        self.assertEqual(3, doubly_linked_list.pop_left())
        self.assertEqual(2, doubly_linked_list.pop_left())
        self.assertEqual(1, doubly_linked_list.pop_left())
        self.assertEqual(0, doubly_linked_list.size)

    def test_pop_right(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.add_left(1)
        doubly_linked_list.add_left(2)
        doubly_linked_list.add_left(3)

        self.assertEqual(1, doubly_linked_list.pop_right())
        self.assertEqual(2, doubly_linked_list.pop_right())
        self.assertEqual(3, doubly_linked_list.pop_right())
        self.assertEqual(0, doubly_linked_list.size)

    def test_remove_val(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.add_left(1)
        doubly_linked_list.add_left(2)
        doubly_linked_list.add_left(3)

        doubly_linked_list.remove_val(2)

        self.assertEqual(3, doubly_linked_list._head.val)
        self.assertEqual(1, doubly_linked_list._head.next.val)
        self.assertEqual(2, doubly_linked_list.size)

    def test_reverse(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.add_right(1)
        doubly_linked_list.add_right(2)
        doubly_linked_list.add_right(3)

        doubly_linked_list.reverse()

        self.assertEqual(3, doubly_linked_list._head.val)
        self.assertEqual(2, doubly_linked_list._head.next.val)
        self.assertEqual(1, doubly_linked_list._head.next.next.val)


if __name__ == '__main__':
    unittest.main()
