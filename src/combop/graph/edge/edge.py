import abc
import typing

V = typing.TypeVar("V")


class Edge(abc.ABC, typing.Generic[V]):
    @property
    @abc.abstractmethod
    def vertex_1(self) -> V:  # pragma: no cover
        pass

    @property
    @abc.abstractmethod
    def vertex_2(self) -> V:  # pragma: no cover
        pass
