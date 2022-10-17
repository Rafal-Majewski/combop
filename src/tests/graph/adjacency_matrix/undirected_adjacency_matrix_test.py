import typing
import unittest

from src.combop.graph.adjacency_matrix import UndirectedAdjacencyMatrix
from src.combop.graph.edge.undirected_edge import UndirectedEdge


class UndirectedAdjacencyMatrixTest(unittest.TestCase):
    def test(self) -> None:
        adjacency_matrix: typing.Final[
            UndirectedAdjacencyMatrix[int, UndirectedEdge[int]]
        ] = UndirectedAdjacencyMatrix()
        vertex_1: typing.Final[int] = 1
        vertex_2: typing.Final[int] = 2
        edge: typing.Final[UndirectedEdge[int]] = UndirectedEdge(vertex_1, vertex_2)
        adjacency_matrix.add_vertex(vertex_1)
        adjacency_matrix.add_vertex(vertex_2)
        adjacency_matrix.add_edge(edge)
        self.assertEqual(
            adjacency_matrix.get_edges_from_to(vertex_1, vertex_2), set([edge])
        )
        self.assertEqual(
            adjacency_matrix.get_edges_from_to(vertex_2, vertex_1), set([edge])
        )
        self.assertEqual(
            adjacency_matrix.get_edges_between(vertex_1, vertex_2), set([edge])
        )
        self.assertEqual(
            adjacency_matrix.get_edges_between(vertex_2, vertex_1), set([edge])
        )
        self.assertEqual(adjacency_matrix.get_edges_from(vertex_1), set([edge]))
        self.assertEqual(adjacency_matrix.get_edges_from(vertex_2), set([edge]))
        self.assertEqual(adjacency_matrix.get_edges_to(vertex_1), set([edge]))
        self.assertEqual(adjacency_matrix.get_edges_to(vertex_2), set([edge]))
        self.assertEqual(adjacency_matrix.get_vertices(), set([vertex_1, vertex_2]))
        adjacency_matrix.remove_edge(edge)
        self.assertEqual(adjacency_matrix.get_edges_from_to(vertex_1, vertex_2), set())
