import unittest

from topological_sort import topological_sort
from data_structures.directed_graph_unweighted import DirectedGraphUnweighted


class TopologicalSortTest(unittest.TestCase):

    def test_topological_sort(self):
        """
        a--->b--->c
             |    ^
             |    |
             ---->d
        """
        graph = DirectedGraphUnweighted()

        graph.add_vertex("a")
        graph.add_vertex("b")
        graph.add_vertex("c")
        graph.add_vertex("d")

        graph.connect("a", "b")
        graph.connect("b", "c")
        graph.connect("b", "d")
        graph.connect("d", "c")

        expected_topological_sort = ["a", "b", "d", "c"]

        actual_topological_sort = topological_sort(graph)

        self.assertListEqual(expected_topological_sort, actual_topological_sort)

    def test_topological_sort_detectsLoop(self):
        """
        a--->b<--->c
             |     ^
             |     |
             ----->d
        """
        graph = DirectedGraphUnweighted()

        graph.add_vertex("a")
        graph.add_vertex("b")
        graph.add_vertex("c")
        graph.add_vertex("d")

        graph.connect("a", "b")
        graph.connect("b", "c")
        graph.connect("b", "d")
        graph.connect("d", "c")
        graph.connect("c", "b")

        actual_topological_sort = topological_sort(graph)

        self.assertIsNone(actual_topological_sort)


if __name__ == '__main__':
    unittest.main()
