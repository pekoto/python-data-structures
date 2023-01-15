import unittest
from problems import topological_sort


class TopologicalSortTest(unittest.TestCase):
    def test_topological_sort(self):
        self.assertEqual([3, 2, 0, 1], topological_sort.topological_sort([[3, 2], [3, 0], [2, 0], [2, 1]]))

    def test_can_schedule(self):
        self.assertTrue(topological_sort.can_schedule([[0, 1], [1, 2]]))
        self.assertFalse(topological_sort.can_schedule([[0, 1], [1, 2], [2, 0]]))
        self.assertTrue(topological_sort.can_schedule([[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]))

    def test_task_schedule(self):
        self.assertEqual([0, 1, 2], topological_sort.task_schedule([[0, 1], [1, 2]]))
        self.assertEqual([], topological_sort.task_schedule([[0, 1], [1, 2], [2, 0]]))
        self.assertEqual([0, 1, 4, 3, 2, 5], topological_sort.task_schedule([[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]))

    def test_all_task_schedules(self):
        self.assertEqual([[0, 1, 2]], topological_sort.all_task_schedules([[0, 1], [1, 2]]))
        self.assertEqual([[3, 2, 0, 1], [3, 2, 1, 0]], topological_sort.all_task_schedules([[3, 2], [3, 0], [2, 0], [2, 1]]))

    def test_alien_dictionary(self):
        self.assertEqual('bac', topological_sort.alien_dictionary(["ba", "bc", "ac", "cab"]))
        self.assertEqual('cab', topological_sort.alien_dictionary(["cab", "aaa", "aab"]))
        self.assertEqual('ywxz', topological_sort.alien_dictionary(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))

    def test_reconstruct_sequence(self):
        self.assertTrue(topological_sort.reconstruct_sequence([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]]))
        self.assertFalse(topological_sort.reconstruct_sequence([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]]))
        self.assertTrue(topological_sort.reconstruct_sequence([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]]))


if __name__ == '__main__':
    unittest.main()
