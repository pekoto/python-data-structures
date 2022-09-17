import unittest

from trie import Trie


class TrieTest(unittest.TestCase):

    def test_get(self):
        trie = Trie()

        trie.add("Dog", "Dog")
        trie.add("Cat", "Cat")
        trie.add("Caterpillar", "Caterpillar")
        trie.add("Doge", "Doge")

        self.assertEqual("Dog", trie.get("Dog"))
        self.assertEqual("Cat", trie.get("Cat"))
        self.assertEqual("Caterpillar", trie.get("Caterpillar"))
        self.assertEqual("Doge", trie.get("Doge"))


if __name__ == '__main__':
    unittest.main()