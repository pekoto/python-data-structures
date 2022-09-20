import unittest

from binary_search_tree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    def test_add(self):
        binary_search_tree = BinarySearchTree()

        binary_search_tree.add(2, 2)
        binary_search_tree.add(1, 1)
        binary_search_tree.add(3, 3)

        self.assertEqual(3, binary_search_tree.size())

    def test_get(self):
        binary_search_tree = BinarySearchTree()

        binary_search_tree.add(2, 'two')
        binary_search_tree.add(1, 'one')
        binary_search_tree.add(3, 'three')

        self.assertEqual('two', binary_search_tree.get(2))
        self.assertEqual('one', binary_search_tree.get(1))
        self.assertEqual('three', binary_search_tree.get(3))

    def test_remove(self):
        binary_search_tree = BinarySearchTree()
        binary_search_tree.add(10, "10")
        binary_search_tree.add(5, "5")
        binary_search_tree.add(1, "1")
        binary_search_tree.add(20, "20")
        binary_search_tree.add(50, "50")
        binary_search_tree.add(7, "7")

        binary_search_tree.remove(10)  # Removes root
        binary_search_tree.remove(50)  # Removes max node
        binary_search_tree.remove(1)   # Removes min node

        with self.assertRaises(KeyError):
            binary_search_tree.get(10)

        with self.assertRaises(KeyError):
            binary_search_tree.get(50)

        with self.assertRaises(KeyError):
            binary_search_tree.get(1)

        self.assertEqual("5", binary_search_tree.get(5))
        self.assertEqual("20", binary_search_tree.get(20))
        self.assertEqual("7", binary_search_tree.get(7))

    def test_is_valid(self):
        bst = BinarySearchTree()
        bst.add(10, "10")
        bst.add(5, "5")
        bst.add(1, "1")
        bst.add(20, "20")
        bst.add(50, "50")
        bst.add(7, "7")

        self.assertTrue(bst.is_valid())


if __name__ == '__main__':
    unittest.main()
