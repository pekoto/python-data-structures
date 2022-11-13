import unittest
import merge_intervals


class MergeIntervalsTest(unittest.TestCase):

    def test_merge_intervals(self):
        self.assertListEqual([[1, 5], [7, 9]], merge_intervals.merge_intervals_a([[1, 4], [2, 5], [7, 9]]))
        self.assertListEqual([[2, 4], [5, 9]], merge_intervals.merge_intervals_a([[6, 7], [2, 4], [5, 9]]))
        self.assertListEqual([[1, 6]], merge_intervals.merge_intervals_a([[1, 4], [2, 6], [3, 5]]))

    def test_insert_interval(self):
        self.assertListEqual([[1, 3], [4, 7], [8, 12]], merge_intervals.insert_interval([[1, 3], [5, 7], [8, 12]], [4, 6]))
        self.assertListEqual([[1, 3], [4, 12]], merge_intervals.insert_interval([[1, 3], [5, 7], [8, 12]], [4, 10]))
        self.assertListEqual([[1, 4], [5, 7]], merge_intervals.insert_interval([[2, 3],[5, 7]], [1, 4]))

    def test_insert_interval_b(self):
        self.assertListEqual([[1, 3], [4, 7], [8, 12]], merge_intervals.insert_interval_b([[1, 3], [5, 7], [8, 12]], [4, 6]))
        self.assertListEqual([[1, 3], [4, 12]], merge_intervals.insert_interval_b([[1, 3], [5, 7], [8, 12]], [4, 10]))
        self.assertListEqual([[1, 4], [5, 7]], merge_intervals.insert_interval_b([[2, 3],[5, 7]], [1, 4]))

    def test_intervals_intersection(self):
        self.assertListEqual([[2, 3], [5, 6], [7, 7]], merge_intervals.intervals_intersection([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]]))
        self.assertListEqual([[5, 7], [9, 10]], merge_intervals.intervals_intersection([[1, 3], [5, 7], [9, 12]], [[5, 10]]))

    def test_conflicting_appointments(self):
        self.assertFalse(merge_intervals.conflicting_appointments([[1, 4], [2, 5], [7, 9]]))
        self.assertTrue(merge_intervals.conflicting_appointments([[6, 7], [2, 4], [8, 12]]))
        self.assertFalse(merge_intervals.conflicting_appointments([[1, 4], [2, 5], [7, 9]]))

    def test_min_meeting_rooms(self):
        self.assertEqual(2, merge_intervals.min_meeting_rooms([[1, 4], [2, 5], [7, 9]]))
        self.assertEqual(1, merge_intervals.min_meeting_rooms([[6, 7], [2, 4], [8, 12]]))
        self.assertEqual(2, merge_intervals.min_meeting_rooms([[1, 4], [2, 3], [3, 6]]))
        self.assertEqual(2, merge_intervals.min_meeting_rooms([[4, 5], [2, 3], [2, 4], [3, 5]]))

    def test_max_cpu_load(self):
        self.assertEqual(7, merge_intervals.max_cpu_load([[1, 4, 3], [2, 5, 4], [7, 9, 6]]))
        self.assertEqual(15, merge_intervals.max_cpu_load([[6, 7, 10], [2, 4, 11], [8, 12, 15]]))
        self.assertEqual(8, merge_intervals.max_cpu_load([[1, 4, 2], [2, 4, 1], [3, 6, 5]]))


if __name__ == '__main__':
    unittest.main()
