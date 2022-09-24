import unittest
from binary_search import binary_search


class BinarySearchTest(unittest.TestCase):
    def test_binary_search_found(self):
        index = binary_search([2, 5, 9, 12, 42, 512], 9)

        self.assertEqual(2, index)

    def test_binary_search_not_found(self):
        with self.assertRaises(KeyError):
            binary_search([2, 5, 9, 12, 42, 512], 13)

    def test_binary_search_found_at_leftmost_pos(self):
        index = binary_search([2, 5, 9, 12, 42, 512], 2)

        self.assertEqual(0, index)

    def test_binary_search_found_at_rightmost_pos(self):
        index = binary_search([2, 5, 9, 12, 42, 512], 512)

        self.assertEqual(5, index)

    def test_binary_search_found_in_odd_array(self):
        index = binary_search([2, 5, 9, 42, 512], 5)

        self.assertEqual(1, index)


if __name__ == '__main__':
    unittest.main()
