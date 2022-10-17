import typing
import unittest

from src.combop.graph.edge.directed_edge import DirectedEdge


class DirectedEdgeTest(unittest.TestCase):
    def test_get_vertex_1(self) -> None:
        starting_vertex: typing.Final[int] = 1
        ending_vertex: typing.Final[int] = 2
        directed_edge: typing.Final[DirectedEdge[int]] = DirectedEdge(
            starting_vertex, ending_vertex
        )
        self.assertIn(directed_edge.vertex_1, set([starting_vertex, ending_vertex]))

    def test_get_vertex_2(self) -> None:
        starting_vertex: typing.Final[int] = 1
        ending_vertex: typing.Final[int] = 2
        directed_edge: typing.Final[DirectedEdge[int]] = DirectedEdge(
            starting_vertex, ending_vertex
        )
        self.assertIn(directed_edge.vertex_2, set([starting_vertex, ending_vertex]))

    def test_get_starting_vertex(self) -> None:
        starting_vertex: typing.Final[int] = 1
        ending_vertex: typing.Final[int] = 2
        directed_edge: typing.Final[DirectedEdge[int]] = DirectedEdge(
            starting_vertex, ending_vertex
        )
        self.assertEqual(directed_edge.starting_vertex, starting_vertex)

    def test_get_ending_vertex(self) -> None:
        starting_vertex: typing.Final[int] = 1
        ending_vertex: typing.Final[int] = 2
        directed_edge: typing.Final[DirectedEdge[int]] = DirectedEdge(
            starting_vertex, ending_vertex
        )
        self.assertEqual(directed_edge.ending_vertex, ending_vertex)
