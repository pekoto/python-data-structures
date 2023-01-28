import unittest
from problems import dynamic_longest_palindromic_seq


class TestDynamicLongestPalindromicSeq(unittest.TestCase):
    def test_longest_palindromic_sequence(self):
        self.assertEqual(5, dynamic_longest_palindromic_seq.longest_palindromic_sequence('abdbca'))
        self.assertEqual(3, dynamic_longest_palindromic_seq.longest_palindromic_sequence('cddpd'))
        self.assertEqual(1, dynamic_longest_palindromic_seq.longest_palindromic_sequence('pqr'))

    def test_longest_palindromic_sequence_topdown(self):
        self.assertEqual(5, dynamic_longest_palindromic_seq.longest_palindromic_sequence_topdown('abdbca'))
        self.assertEqual(3, dynamic_longest_palindromic_seq.longest_palindromic_sequence_topdown('cddpd'))
        self.assertEqual(1, dynamic_longest_palindromic_seq.longest_palindromic_sequence_topdown('pqr'))

    def test_longest_palindromic_sequence_bottomup(self):
        self.assertEqual(5, dynamic_longest_palindromic_seq.longest_palindromic_sequence_bottomup('abdbca'))
        self.assertEqual(3, dynamic_longest_palindromic_seq.longest_palindromic_sequence_bottomup('cddpd'))
        self.assertEqual(1, dynamic_longest_palindromic_seq.longest_palindromic_sequence_bottomup('pqr'))

    def test_longest_palindromic_substr(self):
        self.assertEqual(3, dynamic_longest_palindromic_seq.longest_palindromic_substr('abdbca'))
        self.assertEqual(3, dynamic_longest_palindromic_seq.longest_palindromic_substr('cddpd'))
        self.assertEqual(1, dynamic_longest_palindromic_seq.longest_palindromic_substr('pqr'))

    def test_longest_palindromic_substr_topdown(self):
        self.assertEqual(3, dynamic_longest_palindromic_seq.longest_palindromic_substr_topdown('abdbca'))
        self.assertEqual(3, dynamic_longest_palindromic_seq.longest_palindromic_substr_topdown('cddpd'))
        self.assertEqual(1, dynamic_longest_palindromic_seq.longest_palindromic_substr_topdown('pqr'))

    def test_count_palindromic_substr(self):
        self.assertEqual(7, dynamic_longest_palindromic_seq.count_palindromic_substr('abdbca'))
        self.assertEqual(7, dynamic_longest_palindromic_seq.count_palindromic_substr('cddpd'))
        self.assertEqual(3, dynamic_longest_palindromic_seq.count_palindromic_substr('pqr'))

    def test_count_palindromic_substr_simple(self):
        self.assertEqual(7, dynamic_longest_palindromic_seq.count_palindromic_substr_simple('abdbca'))
        self.assertEqual(7, dynamic_longest_palindromic_seq.count_palindromic_substr_simple('cddpd'))
        self.assertEqual(3, dynamic_longest_palindromic_seq.count_palindromic_substr_simple('pqr'))

    def test_minimum_deletions(self):
        self.assertEqual(1, dynamic_longest_palindromic_seq.minimum_deletions('abdbca'))
        self.assertEqual(2, dynamic_longest_palindromic_seq.minimum_deletions('cddpd'))
        self.assertEqual(2, dynamic_longest_palindromic_seq.minimum_deletions('pqr'))

    def test_minimum_deletions_topdown(self):
        self.assertEqual(1, dynamic_longest_palindromic_seq.minimum_deletions_topdown('abdbca'))
        self.assertEqual(2, dynamic_longest_palindromic_seq.minimum_deletions_topdown('cddpd'))
        self.assertEqual(2, dynamic_longest_palindromic_seq.minimum_deletions_topdown('pqr'))

    def test_palindrome_partitioning(self):
        self.assertEqual(3, dynamic_longest_palindromic_seq.palindrome_partitioning('abdbca'))
        self.assertEqual(2, dynamic_longest_palindromic_seq.palindrome_partitioning('cddpd'))
        self.assertEqual(2, dynamic_longest_palindromic_seq.palindrome_partitioning('pqr'))
        self.assertEqual(0, dynamic_longest_palindromic_seq.palindrome_partitioning('pp'))


if __name__ == '__main__':
    unittest.main()
