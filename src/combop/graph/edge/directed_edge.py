import typing

from .edge import Edge

V = typing.TypeVar("V")


class DirectedEdge(Edge, typing.Generic[V]):
    def __init__(self, starting_vertex: V, ending_vertex: V) -> None:
        self.__starting_vertex: typing.Final[V] = starting_vertex
        self.__ending_vertex: typing.Final[V] = ending_vertex

    @property
    def starting_vertex(self) -> V:
        return self.__starting_vertex

    @property
    def ending_vertex(self) -> V:
        return self.__ending_vertex

    # @override
    @property
    def vertex_1(self) -> V:
        return self.__starting_vertex

    # @override
    @property
    def vertex_2(self) -> V:
        return self.__ending_vertex
