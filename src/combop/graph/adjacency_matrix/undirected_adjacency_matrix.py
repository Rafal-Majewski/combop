import abc
import typing

from ..edge import UndirectedEdge

V = typing.TypeVar("V")
E = typing.TypeVar("E", bound=UndirectedEdge)


class UndirectedAdjacencyMatrix(abc.ABC, typing.Generic[V, E]):
    def __init__(self) -> None:
        self.__data: typing.Final[dict[V, dict[V, set[E]]]] = dict()

    def get_vertices(self) -> set[V]:
        return set(self.__data.keys())

    def __initialize_edges_set(self, tar_vertex_1: V, tar_vertex_2: V) -> None:
        edges_set: typing.Final[set[E]] = set()
        self.__data[tar_vertex_1][tar_vertex_2] = edges_set
        self.__data[tar_vertex_2][tar_vertex_1] = edges_set

    def add_vertex(self, new_vertex: V) -> None:
        self.__data[new_vertex] = dict()
        for vertex in self.__data.keys():
            self.__initialize_edges_set(new_vertex, vertex)

    def add_edge(self, new_edge: E) -> None:
        vertex_1: typing.Final[V] = new_edge.vertex_1
        vertex_2: typing.Final[V] = new_edge.vertex_2
        self.__data[vertex_1][vertex_2].add(new_edge)

    def remove_edge(self, rem_edge: E) -> None:
        vertex_1: typing.Final[V] = rem_edge.vertex_1
        vertex_2: typing.Final[V] = rem_edge.vertex_2
        self.__data[vertex_1][vertex_2].remove(rem_edge)

    # override
    def get_edges_from_to(self, tar_vertex_1: V, tar_vertex_2: V) -> set[E]:
        edges: typing.Final[set[E]] = set()
        edges.update(self.__data[tar_vertex_1][tar_vertex_2])
        return edges

    def get_edges_between(self, tar_vertex_1: V, tar_vertex_2: V) -> set[E]:
        return self.get_edges_from_to(tar_vertex_1, tar_vertex_2)

    def get_edges_from(self, tar_vertex: V) -> set[E]:
        edges: typing.Final[set[E]] = set()
        for vertex in self.__data.keys():
            edges.update(self.__data[tar_vertex][vertex])
        return edges

    def get_edges_to(self, tar_vertex: V) -> set[E]:
        edges: typing.Final[set[E]] = set()
        for vertex in self.__data.keys():
            edges.update(self.__data[vertex][tar_vertex])
        return edges
