import unittest
import fast_and_slow
from fast_and_slow import Node


class FastAndSlowTest(unittest.TestCase):

    def test_fast_and_slow(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)
        self.assertFalse(fast_and_slow.has_cycle(head))

        head.next.next.next.next.next.next = head.next.next
        self.assertTrue(fast_and_slow.has_cycle(head))

        head.next.next.next.next.next.next = head.next.next.next
        self.assertTrue(fast_and_slow.has_cycle(head))

    def test_cycle_length(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)
        head.next.next.next.next.next.next = head.next.next
        self.assertEqual(4, fast_and_slow.cycle_length(head))

        head.next.next.next.next.next.next = head.next.next.next
        self.assertEqual(3, fast_and_slow.cycle_length(head))

    def test_start_of_cycle(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)

        head.next.next.next.next.next.next = head.next.next
        self.assertEqual(head.next.next, fast_and_slow.start_of_cycle(head))

    def test_is_happy(self):
        self.assertTrue(fast_and_slow.is_happy(23))
        self.assertFalse(fast_and_slow.is_happy(12))

    def test_middle_of_linked_list(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)

        self.assertEqual(head.next.next, fast_and_slow.find_middle_of_linked_list(head))

        head.next.next.next.next.next = Node(6)
        self.assertEqual(head.next.next.next, fast_and_slow.find_middle_of_linked_list(head))

        head.next.next.next.next.next.next = Node(7)
        self.assertEqual(head.next.next.next, fast_and_slow.find_middle_of_linked_list(head))

    def test_linked_list_palindrome(self):
        head = Node(2)
        head.next = Node(4)
        head.next.next = Node(6)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(2)
        self.assertTrue(fast_and_slow.linked_list_palindrome(head))

        head.next.next.next.next.next = Node(2)
        self.assertFalse(fast_and_slow.linked_list_palindrome(head))

    def test_interleave_linked_lists(self):
        head = Node(2)
        head.next = Node(4)
        head.next.next = Node(6)
        head.next.next.next = Node(8)
        head.next.next.next.next = Node(10)
        head.next.next.next.next.next = Node(12)

        fast_and_slow.interleave_linked_list(head)

        self.assertEqual(2, head.value)
        self.assertEqual(12, head.next.value)
        self.assertEqual(4, head.next.next.value)
        self.assertEqual(10, head.next.next.next.value)
        self.assertEqual(6, head.next.next.next.next.value)
        self.assertEqual(8, head.next.next.next.next.next.value)
        self.assertIsNone(head.next.next.next.next.next.next)

        head = Node(2)
        head.next = Node(4)
        head.next.next = Node(6)
        head.next.next.next = Node(8)
        head.next.next.next.next = Node(10)

        fast_and_slow.interleave_linked_list(head)

        self.assertEqual(2, head.value)
        self.assertEqual(10, head.next.value)
        self.assertEqual(4, head.next.next.value)
        self.assertEqual(8, head.next.next.next.value)
        self.assertEqual(6, head.next.next.next.next.value)
        self.assertIsNone(head.next.next.next.next.next)


if __name__ == '__main__':
    unittest.main()
