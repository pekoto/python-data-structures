import unittest
import subsets


class SubsetsTest(unittest.TestCase):
    def test_generate_subsets(self):
        self.assertListEqual([[], [1], [3], [1, 3]], subsets.generate_subsets([1, 3]))
        self.assertListEqual([[], [1], [5], [1, 5], [3], [1, 3], [5, 3], [1, 5, 3]], subsets.generate_subsets([1, 5, 3]))

    def test_subsets_with_duplicates(self):
        self.assertListEqual([[], [1], [3], [1, 3], [3, 3], [1, 3, 3]], subsets.subsets_with_duplicates([1, 3, 3]))
        self.assertListEqual([[], [1], [3], [1, 3], [3, 3], [1, 3, 3], [5], [1, 5], [3, 5], [1, 3, 5], [3, 3, 5], [1, 3, 3, 5]],
                             subsets.subsets_with_duplicates([1, 5, 3, 3]))

    def test_generate_permutations(self):
        self.assertListEqual([[5, 3, 1], [3, 5, 1], [3, 1, 5], [5, 1, 3], [1, 5, 3], [1, 3, 5]], subsets.generate_permutations([1, 3, 5]))

    def test_case_permutations(self):
        self.assertListEqual(['ad52', 'aD52', 'Ad52', 'AD52'], subsets.case_permutations('ad52'))
        self.assertListEqual(['ab7c', 'ab7C', 'aB7c', 'aB7C', 'Ab7c', 'Ab7C', 'AB7c', 'AB7C'], subsets.case_permutations('ab7c'))

    def test_balanced_parentheses(self):
        self.assertListEqual(['(())', '()()'], subsets.balanced_parentheses(2))
        self.assertListEqual(['((()))', '(()())', '(())()', '()(())', '()()()'], subsets.balanced_parentheses(3))


if __name__ == '__main__':
    unittest.main()
