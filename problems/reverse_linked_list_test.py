import unittest

from problems import reverse_linked_list
from problems.reverse_linked_list import Node


class ReverseLinkedListTest(unittest.TestCase):

    def test_reverse_linked_list(self):
        head = Node(2)
        head.next = Node(4)
        head.next.next = Node(6)
        head.next.next.next = Node(8)
        head.next.next.next.next = Node(10)

        reversed_list = reverse_linked_list.reverse_linked_list(head)

        self.assertEqual(10, reversed_list.value)
        self.assertEqual(8, reversed_list.next.value)
        self.assertEqual(6, reversed_list.next.next.value)
        self.assertEqual(4, reversed_list.next.next.next.value)
        self.assertEqual(2, reversed_list.next.next.next.next.value)
        self.assertIsNone(reversed_list.next.next.next.next.next)

    def test_reverse_sublist(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)

        reversed_sublist = reverse_linked_list.reverse_sublist(head, 2, 4)

        self.assertEqual(1, reversed_sublist.value)
        self.assertEqual(4, reversed_sublist.next.value)
        self.assertEqual(3, reversed_sublist.next.next.value)
        self.assertEqual(2, reversed_sublist.next.next.next.value)
        self.assertEqual(5, reversed_sublist.next.next.next.next.value)
        self.assertIsNone(reversed_sublist.next.next.next.next.next)

    def test_reverse_k_element_sublist(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)
        head.next.next.next.next.next.next = Node(7)
        head.next.next.next.next.next.next.next = Node(8)

        reversed_sublist = reverse_linked_list.reverse_k_element_sublist(head, 3)

        self.assertEqual(3, reversed_sublist.value)
        self.assertEqual(2, reversed_sublist.next.value)
        self.assertEqual(1, reversed_sublist.next.next.value)
        self.assertEqual(6, reversed_sublist.next.next.next.value)
        self.assertEqual(5, reversed_sublist.next.next.next.next.value)
        self.assertEqual(4, reversed_sublist.next.next.next.next.next.value)
        self.assertEqual(8, reversed_sublist.next.next.next.next.next.next.value)
        self.assertEqual(7, reversed_sublist.next.next.next.next.next.next.next.value)
        self.assertIsNone(reversed_sublist.next.next.next.next.next.next.next.next)

    def test_reverse_alternating_k_element_sublist(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)
        head.next.next.next.next.next.next = Node(7)
        head.next.next.next.next.next.next.next = Node(8)

        reversed_sublist = reverse_linked_list.reverse_alternating_k_element_sublist(head, 2)

        self.assertEqual(2, reversed_sublist.value)
        self.assertEqual(1, reversed_sublist.next.value)
        self.assertEqual(3, reversed_sublist.next.next.value)
        self.assertEqual(4, reversed_sublist.next.next.next.value)
        self.assertEqual(6, reversed_sublist.next.next.next.next.value)
        self.assertEqual(5, reversed_sublist.next.next.next.next.next.value)
        self.assertEqual(7, reversed_sublist.next.next.next.next.next.next.value)
        self.assertEqual(8, reversed_sublist.next.next.next.next.next.next.next.value)
        self.assertIsNone(reversed_sublist.next.next.next.next.next.next.next.next)

    def test_rotate_linked_list(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)

        new_head = reverse_linked_list.rotate_linked_list_2(head, 3)

        self.assertEqual(4, new_head.value)
        self.assertEqual(5, new_head.next.value)
        self.assertEqual(6, new_head.next.next.value)
        self.assertEqual(1, new_head.next.next.next.value)
        self.assertEqual(2, new_head.next.next.next.next.value)
        self.assertEqual(3, new_head.next.next.next.next.next.value)
        self.assertIsNone(new_head.next.next.next.next.next.next)

        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)

        new_head = reverse_linked_list.rotate_linked_list_2(head, 8)

        self.assertEqual(3, new_head.value)
        self.assertEqual(4, new_head.next.value)
        self.assertEqual(5, new_head.next.next.value)
        self.assertEqual(1, new_head.next.next.next.value)
        self.assertEqual(2, new_head.next.next.next.next.value)
        self.assertIsNone(new_head.next.next.next.next.next)


if __name__ == '__main__':
    unittest.main()
