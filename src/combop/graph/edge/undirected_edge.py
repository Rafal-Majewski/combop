import typing

from .edge import Edge

V = typing.TypeVar("V")


class UndirectedEdge(Edge, typing.Generic[V]):
    def __init__(self, vertex_1: V, ending_vertex: V) -> None:
        self.__vertex_1: typing.Final[V] = vertex_1
        self.__vertex_2: typing.Final[V] = ending_vertex

    # @override
    @property
    def vertex_1(self) -> V:
        return self.__vertex_1

    # @override
    @property
    def vertex_2(self) -> V:
        return self.__vertex_2
