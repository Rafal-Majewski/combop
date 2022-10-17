import typing
import unittest

from src.combop.graph.edge.undirected_edge import UndirectedEdge


class UndirectedEdgeTest(unittest.TestCase):
    def test_get_vertex_1(self) -> None:
        starting_vertex: typing.Final[int] = 1
        ending_vertex: typing.Final[int] = 2
        undirected_edge: typing.Final[UndirectedEdge[int]] = UndirectedEdge(
            starting_vertex, ending_vertex
        )
        self.assertIn(undirected_edge.vertex_1, set([starting_vertex, ending_vertex]))

    def test_get_vertex_2(self) -> None:
        starting_vertex: typing.Final[int] = 1
        ending_vertex: typing.Final[int] = 2
        undirected_edge: typing.Final[UndirectedEdge[int]] = UndirectedEdge(
            starting_vertex, ending_vertex
        )
        self.assertIn(undirected_edge.vertex_2, set([starting_vertex, ending_vertex]))
