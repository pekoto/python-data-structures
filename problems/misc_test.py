import unittest
import misc


class MiscTest(unittest.TestCase):
    def test_get_valid_partitions(self):
        self.assertEqual([["ad", "age"], ["adage"]],
                         misc.get_valid_partitions("adage", set(["ad", "age", "adage", "a"])))

    def test_number_of_provinces(self):
        self.assertEqual(2, misc.number_of_provinces([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
        self.assertEqual(3, misc.number_of_provinces([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
        self.assertEqual(3, misc.number_of_provinces([[1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1]]))

    def test_number_of_provinces_union_find(self):
        self.assertEqual(2, misc.number_of_provinces_union_find([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
        self.assertEqual(3, misc.number_of_provinces_union_find([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
        self.assertEqual(3, misc.number_of_provinces_union_find([[1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1]]))


if __name__ == '__main__':
    unittest.main()
