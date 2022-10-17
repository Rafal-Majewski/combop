from __future__ import annotations

import typing

from .edge import UndirectedEdge
from .graph import Graph

V = typing.TypeVar("V")
E = typing.TypeVar("E", bound=UndirectedEdge)


class UndirectedGraph(Graph[V, E], typing.Generic[V, E]):
    def __init__(self) -> None:
        self.__adjacency_matrix: typing.Final[dict[V, dict[V, set[E]]]] = dict()

    def get_vertices(self) -> set[V]:
        return set(self.__adjacency_matrix.keys())

    def __initialize_edges_set(self, tar_vertex_1: V, tar_vertex_2: V) -> None:
        edges_set: typing.Final[set[E]] = set()
        self.__adjacency_matrix[tar_vertex_1][tar_vertex_2] = edges_set
        self.__adjacency_matrix[tar_vertex_2][tar_vertex_1] = edges_set

    def add_vertex(self, new_vertex: V) -> None:
        self.__adjacency_matrix[new_vertex] = dict()
        for vertex in self.__adjacency_matrix.keys():
            self.__initialize_edges_set(new_vertex, vertex)

    def add_edge(self, new_edge: E) -> None:
        vertex_1: typing.Final[V] = new_edge.vertex_1
        vertex_2: typing.Final[V] = new_edge.vertex_2
        self.__adjacency_matrix[vertex_1][vertex_2].add(new_edge)

    def remove_edge(self, rem_edge: E) -> None:
        vertex_1: typing.Final[V] = rem_edge.vertex_1
        vertex_2: typing.Final[V] = rem_edge.vertex_2
        self.__adjacency_matrix[vertex_1][vertex_2].remove(rem_edge)

    def get_edges_from_to(self, tar_vertex_1: V, tar_vertex_2: V) -> set[E]:
        edges: typing.Final[set[E]] = set()
        edges.update(self.__adjacency_matrix[tar_vertex_1][tar_vertex_2])
        return edges

    def get_edges_between(self, tar_vertex_1: V, tar_vertex_2: V) -> set[E]:
        return self.get_edges_from_to(tar_vertex_1, tar_vertex_2)

    def get_edges_from(self, tar_vertex: V) -> set[E]:
        edges: typing.Final[set[E]] = set()
        for vertex in self.__adjacency_matrix.keys():
            edges.update(self.__adjacency_matrix[tar_vertex][vertex])
        return edges

    def get_edges_to(self, tar_vertex: V) -> set[E]:
        edges: typing.Final[set[E]] = set()
        for vertex in self.__adjacency_matrix.keys():
            edges.update(self.__adjacency_matrix[vertex][tar_vertex])
        return edges

    def get_edges(self) -> set[E]:
        edges: typing.Final[set[E]] = set()
        for vertex_1 in self.__adjacency_matrix.keys():
            for vertex_2 in self.__adjacency_matrix.keys():
                edges.update(self.__adjacency_matrix[vertex_1][vertex_2])
        return edges
