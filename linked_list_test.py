import unittest

from linked_list import LinkedList


class LinkedListTest(unittest.TestCase):

    def test_add_recursive(self):
        linked_list = LinkedList()
        linked_list.add_recursive(1)
        linked_list.add_recursive(2)
        linked_list.add_recursive(3)

        self.assertEqual(3, linked_list.size)
        self.assertEqual(1, linked_list._head.val)
        self.assertEqual(2, linked_list._head.next.val)
        self.assertEqual(3, linked_list._head.next.next.val)

    def test_add_iterative(self):
        linked_list = LinkedList()
        linked_list.add_iterative(1)
        linked_list.add_iterative(2)
        linked_list.add_iterative(3)

        self.assertEqual(3, linked_list.size)
        self.assertEqual(1, linked_list._head.val)
        self.assertEqual(2, linked_list._head.next.val)
        self.assertEqual(3, linked_list._head.next.next.val)

    def test_remove_recursive(self):
        linked_list = LinkedList()
        linked_list.add_iterative(1)
        linked_list.add_iterative(2)
        linked_list.add_iterative(3)

        linked_list.remove_recursive(2)

        self.assertEqual(2, linked_list.size)
        self.assertEqual(1, linked_list._head.val)
        self.assertEqual(3, linked_list._head.next.val)

    def test_remove_iterative(self):
        linked_list = LinkedList()
        linked_list.add_iterative(1)
        linked_list.add_iterative(2)
        linked_list.add_iterative(3)

        linked_list.remove_iterative(2)

        self.assertEqual(2, linked_list.size)
        self.assertEqual(1, linked_list._head.val)
        self.assertEqual(3, linked_list._head.next.val)

    def test_reverse(self):
        linked_list = LinkedList()
        linked_list.add_iterative(1)
        linked_list.add_iterative(2)
        linked_list.add_iterative(3)

        linked_list.reverse()

        self.assertEqual(3, linked_list.size)
        self.assertEqual(3, linked_list._head.val)
        self.assertEqual(2, linked_list._head.next.val)
        self.assertEqual(1, linked_list._head.next.next.val)


if __name__ == '__main__':
    unittest.main()
