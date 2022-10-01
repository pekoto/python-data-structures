import unittest

from .dijkstras_algorithm import DijkstrasAlgorithm
from data_structures.directed_graph_weighted import DirectedGraphWeighted


class DijkstrasAlgorithmTest(unittest.TestCase):

    def test_dijkstras_algorithm(self):
        """Basically we need to test all methods together.
        The graph should look like this:
           6      5
        a-----b------
        |     |     |
      1 |  2/ | 2   c
        | /   |     |
        d-----e------
            1     5
        """
        graph = DirectedGraphWeighted()

        graph.add_vertex("a")
        graph.add_vertex("b")
        graph.add_vertex("c")
        graph.add_vertex("d")
        graph.add_vertex("e")

        graph.connect("a", "b", 6.0)
        graph.connect("a", "d", 1.0)

        graph.connect("b", "a", 6.0)
        graph.connect("b", "d", 2.0)
        graph.connect("b", "e", 2.0)
        graph.connect("b", "c", 5.0)

        graph.connect("c", "b", 5.0)
        graph.connect("c", "e", 5.0)

        graph.connect("d", "a", 1.0)
        graph.connect("d", "b", 2.0)
        graph.connect("d", "e", 1.0)

        graph.connect("e", "d", 1.0)
        graph.connect("e", "b", 2.0)
        graph.connect("e", "c", 5.0)

        dijkstras_algorithm = DijkstrasAlgorithm(graph, "a")

        self.assertEqual(0.0, dijkstras_algorithm.distance_to("a"))
        self.assertEqual(3.0, dijkstras_algorithm.distance_to("b"))
        self.assertEqual(7.0, dijkstras_algorithm.distance_to("c"))
        self.assertEqual(1.0, dijkstras_algorithm.distance_to("d"))
        self.assertEqual(2.0, dijkstras_algorithm.distance_to("e"))

        self.assertListEqual(["a", "d", "b"], dijkstras_algorithm.path_to("b"))
        self.assertListEqual(["a", "d", "e", "c"], dijkstras_algorithm.path_to("c"))
        self.assertListEqual(["a", "d"], dijkstras_algorithm.path_to("d"))
        self.assertListEqual(["a", "d", "e"], dijkstras_algorithm.path_to("e"))


if __name__ == '__main__':
    unittest.main()
