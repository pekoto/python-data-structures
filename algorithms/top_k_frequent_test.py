import unittest

from algorithms.top_k_frequent import top_k_frequent


class TopKFrequentTest(unittest.TestCase):

    def test_top_k_frequent_pq(self):
        nums = [1, 1, 1, 2, 2, 2, 7, 4]
        k = 2

        top_k = top_k_frequent(nums, k)

        self.assertListEqual([1, 2], top_k)


if __name__ == '__main__':
    unittest.main()
