import typing
import unittest

from src.combop.graph import UndirectedGraph
from src.combop.graph.edge.undirected_edge import UndirectedEdge


class UndirectedAdjacencyMatrixTest(unittest.TestCase):
    def test(self) -> None:
        graph: typing.Final[
            UndirectedGraph[int, UndirectedEdge[int]]
        ] = UndirectedGraph()
        vertex_1: typing.Final[int] = 1
        vertex_2: typing.Final[int] = 2
        edge: typing.Final[UndirectedEdge[int]] = UndirectedEdge(vertex_1, vertex_2)
        graph.add_vertex(vertex_1)
        graph.add_vertex(vertex_2)
        graph.add_edge(edge)
        self.assertEqual(graph.get_edges_from_to(vertex_1, vertex_2), set([edge]))
        self.assertEqual(graph.get_edges_from_to(vertex_2, vertex_1), set([edge]))
        self.assertEqual(graph.get_edges_between(vertex_1, vertex_2), set([edge]))
        self.assertEqual(graph.get_edges_between(vertex_2, vertex_1), set([edge]))
        self.assertEqual(graph.get_edges_from(vertex_1), set([edge]))
        self.assertEqual(graph.get_edges_from(vertex_2), set([edge]))
        self.assertEqual(graph.get_edges_to(vertex_1), set([edge]))
        self.assertEqual(graph.get_edges_to(vertex_2), set([edge]))
        self.assertEqual(graph.get_vertices(), set([vertex_1, vertex_2]))
        self.assertEqual(graph.get_edges(), set([edge]))
        graph.remove_edge(edge)
        self.assertEqual(graph.get_edges_from_to(vertex_1, vertex_2), set())
