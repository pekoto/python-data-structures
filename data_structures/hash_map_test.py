import unittest

from hash_map import HashMap


class HashMapTest(unittest.TestCase):

    def test_put(self):
        hash_map = HashMap()
        hash_map.put("1", 1)
        hash_map.put("2", 2)
        hash_map.put("3", 3)

        self.assertEquals(3, hash_map.size)

    def test_get(self):
        hash_map = HashMap()
        hash_map.put("1", 1)
        hash_map.put("2", 2)
        hash_map.put("3", 3)

        self.assertEquals(1, hash_map.get("1"))
        self.assertTrue(2, hash_map.get("2"))
        self.assertTrue(3, hash_map.get("3"))

    def test_update_value(self):
        hash_map = HashMap()
        hash_map.put("1", 1)
        hash_map.put("1", "one")

        self.assertEquals("one", hash_map.get("1"))

    def test_delete(self):
        hash_map = HashMap()
        hash_map.put("1", 1)
        hash_map.put("2", 1)
        hash_map.put("3", 1)

        hash_map.delete("2")

        self.assertEquals(2, hash_map.size)

    def test_delete_key_not_found_raises_key_error(self):
        hash_map = HashMap()
        hash_map.put("1", 1)
        hash_map.put("2", 1)
        hash_map.put("3", 1)

        with self.assertRaises(KeyError):
            hash_map.delete("4")

    def test_get_key_not_found_raises_key_error(self):
        hash_map = HashMap()
        hash_map.put("1", 1)
        hash_map.put("2", 1)
        hash_map.put("3", 1)

        with self.assertRaises(KeyError):
            hash_map.get("4")


if __name__ == '__main__':
    unittest.main()