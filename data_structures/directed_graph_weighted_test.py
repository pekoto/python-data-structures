import unittest

from directed_graph_weighted import DirectedGraphWeighted


class DirectedGraphWeightedTest(unittest.TestCase):

    def test_graph(self):
        """Basically we need to test all methods together.
        The graph should look like this:
        a---->b
        |     |
        v     v
        c---->d---->e
        """
        graph = DirectedGraphWeighted()

        graph.add_vertex("a")
        graph.add_vertex("b")
        graph.add_vertex("c")
        graph.add_vertex("d")
        graph.add_vertex("e")

        graph.connect("a", "b", 1.0)
        graph.connect("a", "c", 2.0)
        graph.connect("b", "d", 2.0)
        graph.connect("c", "d", 4.0)
        graph.connect("d", "e", 3.0)

        print(graph._vertices)

        self.assertTrue(graph.is_connected("a", "b"))
        self.assertTrue(graph.is_connected("a", "c"))
        self.assertTrue(graph.is_connected("b", "d"))
        self.assertTrue(graph.is_connected("c", "d"))
        self.assertTrue(graph.is_connected("d", "e"))

        self.assertFalse(graph.is_connected("a", "e"))
        self.assertFalse(graph.is_connected("a", "d"))
        self.assertFalse(graph.is_connected("b", "c"))
        self.assertFalse(graph.is_connected("b", "e"))
        self.assertFalse(graph.is_connected("c", "e"))

        self.assertAlmostEqual(1.0, graph.weight("a", "b"))
        self.assertAlmostEqual(2.0, graph.weight("a", "c"))
        self.assertAlmostEqual(2.0, graph.weight("b", "d"))
        self.assertAlmostEqual(4.0, graph.weight("c", "d"))
        self.assertAlmostEqual(3.0, graph.weight("d", "e"))

    def test_connect_throws_error_if_vertex_not_found(self):
        graph = DirectedGraphWeighted()

        with self.assertRaises(KeyError):
            graph.connect("a", "b", 1.0)

    def test_is_connected_throws_error_if_vertex_not_found(self):
        graph = DirectedGraphWeighted()

        with self.assertRaises(KeyError):
            graph.is_connected("a", "b")

    def test_weight_throws_error_if_vertex_not_found(self):
        graph = DirectedGraphWeighted()

        with self.assertRaises(KeyError):
            graph.weight("a", "b")

    def test_weight_throws_error_if_vertex_not_connected(self):
        graph = DirectedGraphWeighted()

        graph.add_vertex("a")
        graph.add_vertex("b")
        graph.add_vertex("c")

        graph.connect("a", "b", 1.0)

        with self.assertRaises(Exception):
            graph.weight("a", "c")

    def test_vertices(self):
        """Basically we need to test all methods together.
        The graph should look like this:
        a---->b
        |     |
        v     v
        c---->d---->e
        """
        graph = DirectedGraphWeighted()

        graph.add_vertex("a")
        graph.add_vertex("b")
        graph.add_vertex("c")
        graph.add_vertex("d")
        graph.add_vertex("e")

        graph.connect("a", "b", 1.0)
        graph.connect("a", "c", 2.0)
        graph.connect("b", "d", 2.0)
        graph.connect("c", "d", 4.0)
        graph.connect("d", "e", 3.0)

        self.assertListEqual(["a", "b", "c", "d", "e"], graph.vertices())

    def test_neighbours_to(self):
        """Basically we need to test all methods together.
       The graph should look like this:
       a---->b
       |     |
       v     v
       c---->d---->e
       """
        graph = DirectedGraphWeighted()

        graph.add_vertex("a")
        graph.add_vertex("b")
        graph.add_vertex("c")
        graph.add_vertex("d")
        graph.add_vertex("e")

        graph.connect("a", "b", 1.0)
        graph.connect("a", "c", 2.0)
        graph.connect("b", "d", 2.0)
        graph.connect("c", "d", 4.0)
        graph.connect("d", "e", 3.0)

        self.assertEqual({"b": 1.0, "c": 2.0}, graph.neighbours_to("a"))
        self.assertEqual({"d": 2.0}, graph.neighbours_to("b"))
        self.assertEqual({"d": 4.0}, graph.neighbours_to("c"))
        self.assertEqual({"e": 3.0}, graph.neighbours_to("d"))
        self.assertEqual({}, graph.neighbours_to("e"))


if __name__ == '__main__':
    unittest.main()
