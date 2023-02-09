import unittest
from problems import dynamic_longest_common_substr


class LongestCommonSubstrTest(unittest.TestCase):
    def test_longest_common_substring(self):
        self.assertEqual(2, dynamic_longest_common_substr.longest_common_substring('abdca', 'cbda'))
        self.assertEqual(3, dynamic_longest_common_substr.longest_common_substring('passport', 'ppsspt'))

    def test_longest_common_substring_bottomup(self):
        self.assertEqual(2, dynamic_longest_common_substr.longest_common_substring_bottomup('abdca', 'cbda'))
        self.assertEqual(3, dynamic_longest_common_substr.longest_common_substring_bottomup('passport', 'ppsspt'))

    def test_longest_common_subsequence(self):
        self.assertEqual(3, dynamic_longest_common_substr.longest_common_subsequence('abdca', 'cbda'))
        self.assertEqual(5, dynamic_longest_common_substr.longest_common_subsequence('passport', 'ppsspt'))

    def test_longest_common_subsequence_topdown(self):
        self.assertEqual(3, dynamic_longest_common_substr.longest_common_subsequence_topdown('abdca', 'cbda'))
        self.assertEqual(5, dynamic_longest_common_substr.longest_common_subsequence_topdown('passport', 'ppsspt'))

    def test_longest_common_subsequence_bottomup(self):
        self.assertEqual(3, dynamic_longest_common_substr.longest_common_subsequence_bottomup('abdca', 'cbda'))
        self.assertEqual(5, dynamic_longest_common_substr.longest_common_subsequence_bottomup('passport', 'ppsspt'))

    def test_min_deletions_insertions(self):
        self.assertEqual((1, 1), dynamic_longest_common_substr.min_deletions_insertions('abc', 'fbc'))
        self.assertEqual((2, 1), dynamic_longest_common_substr.min_deletions_insertions('abdca', 'cbda'))
        self.assertEqual((3, 1), dynamic_longest_common_substr.min_deletions_insertions('passport', 'ppsspt'))

    def test_longest_increasing_subsequence(self):
        self.assertEqual(5, dynamic_longest_common_substr.longest_increasing_subsequence([4, 2, 3, 6, 10, 1, 12]))
        self.assertEqual(4, dynamic_longest_common_substr.longest_increasing_subsequence([-4, 10, 3, 7, 15]))

    def test_longest_increasing_subsequence_topdown(self):
        self.assertEqual(5, dynamic_longest_common_substr.longest_increasing_subsequence_topdown([4, 2, 3, 6, 10, 1, 12]))
        self.assertEqual(4, dynamic_longest_common_substr.longest_increasing_subsequence_topdown([-4, 10, 3, 7, 15]))

    def test_maximum_sum_increasing_subsequence(self):
        self.assertEqual(32, dynamic_longest_common_substr.maximum_sum_increasing_subsequence([4, 1, 2, 6, 10, 1, 12]))
        self.assertEqual(25, dynamic_longest_common_substr.maximum_sum_increasing_subsequence([-4, 10, 3, 7, 15]))

    def test_maximum_sum_increasing_subsequence_topdown(self):
        self.assertEqual(32, dynamic_longest_common_substr.maximum_sum_increasing_subsequence_topdown([4, 1, 2, 6, 10, 1, 12]))
        self.assertEqual(25, dynamic_longest_common_substr.maximum_sum_increasing_subsequence_topdown([-4, 10, 3, 7, 15]))

    def test_shortest_common_supersequence(self):
        self.assertEqual(5, dynamic_longest_common_substr.shortest_common_supersequence('abcf', 'bdcf'))
        self.assertEqual(15, dynamic_longest_common_substr.shortest_common_supersequence('dynamic', 'programming'))

    def test_shortest_common_supersequence_topdown(self):
        self.assertEqual(5, dynamic_longest_common_substr.shortest_common_supersequence_topdown('abcf', 'bdcf'))
        self.assertEqual(15, dynamic_longest_common_substr.shortest_common_supersequence_topdown('dynamic', 'programming'))

    def test_minimum_deletions_to_sort(self):
        self.assertEqual(2, dynamic_longest_common_substr.minimum_deletions_to_sort([4, 2, 3, 6, 10, 1, 12]))
        self.assertEqual(1, dynamic_longest_common_substr.minimum_deletions_to_sort([-4, 10, 3, 7, 15]))
        self.assertEqual(3, dynamic_longest_common_substr.minimum_deletions_to_sort([3, 2, 1, 0]))

    def test_minimum_deletions_to_sort_topdown(self):
        self.assertEqual(2, dynamic_longest_common_substr.minimum_deletions_to_sort_topdown([4, 2, 3, 6, 10, 1, 12]))
        self.assertEqual(1, dynamic_longest_common_substr.minimum_deletions_to_sort_topdown([-4, 10, 3, 7, 15]))
        self.assertEqual(3, dynamic_longest_common_substr.minimum_deletions_to_sort_topdown([3, 2, 1, 0]))

    def test_longest_repeating_subseq(self):
        self.assertEqual(2, dynamic_longest_common_substr.longest_repeating_subseq('tomorrow'))
        self.assertEqual(3, dynamic_longest_common_substr.longest_repeating_subseq('aabdbced'))
        self.assertEqual(2, dynamic_longest_common_substr.longest_repeating_subseq('fmff'))

    def test_longest_repeating_subseq_topdown(self):
        self.assertEqual(2, dynamic_longest_common_substr.longest_repeating_subseq_topdown('tomorrow'))
        self.assertEqual(3, dynamic_longest_common_substr.longest_repeating_subseq_topdown('aabdbced'))
        self.assertEqual(2, dynamic_longest_common_substr.longest_repeating_subseq_topdown('fmff'))

    def test_subsequence_pattern_matching(self):
        self.assertEqual(2, dynamic_longest_common_substr.subsequence_pattern_matching('baxmx', 'ax'))
        self.assertEqual(4, dynamic_longest_common_substr.subsequence_pattern_matching('tomorrow', 'tor'))

    def test_subsequence_pattern_matching_topdown(self):
        self.assertEqual(2, dynamic_longest_common_substr.subsequence_pattern_matching_topdown('baxmx', 'ax'))
        self.assertEqual(4, dynamic_longest_common_substr.subsequence_pattern_matching_topdown('tomorrow', 'tor'))

    def test_longest_bitonic_subsequence(self):
        self.assertEqual(5, dynamic_longest_common_substr.longest_bitonic_subsequence([4, 2, 3, 6, 10, 1, 12]))
        self.assertEqual(7, dynamic_longest_common_substr.longest_bitonic_subsequence([4, 2, 5, 9, 7, 6, 10, 3, 1]))

    def test_longest_alternating_sequence(self):
        self.assertEqual(2, dynamic_longest_common_substr.longest_alternating_sequence([1, 2, 3, 4]))
        self.assertEqual(3, dynamic_longest_common_substr.longest_alternating_sequence([3, 2, 1, 4]))
        self.assertEqual(4, dynamic_longest_common_substr.longest_alternating_sequence([1, 3, 2, 4]))

    def test_longest_alternating_sequence_topdown(self):
        self.assertEqual(2, dynamic_longest_common_substr.longest_alternating_sequence_topdown([1, 2, 3, 4]))
        self.assertEqual(3, dynamic_longest_common_substr.longest_alternating_sequence_topdown([3, 2, 1, 4]))
        self.assertEqual(4, dynamic_longest_common_substr.longest_alternating_sequence_topdown([1, 3, 2, 4]))

    def test_edit_distance(self):
        self.assertEqual(1, dynamic_longest_common_substr.edit_distance('bat', 'but'))
        self.assertEqual(2, dynamic_longest_common_substr.edit_distance('abdca', 'cbda'))
        self.assertEqual(3, dynamic_longest_common_substr.edit_distance('passpot', 'ppsspqrt'))

    def test_string_interleaving(self):
        self.assertTrue(dynamic_longest_common_substr.string_interleaving('abd', 'cef', 'abcdef'))
        self.assertFalse(dynamic_longest_common_substr.string_interleaving('abd', 'cef', 'abcbef'))
        self.assertFalse(dynamic_longest_common_substr.string_interleaving('abc', 'def', 'abdccf'))
        self.assertTrue(dynamic_longest_common_substr.string_interleaving('abcdef', 'mnop', 'mnaobcdepf'))


if __name__ == '__main__':
    unittest.main()
