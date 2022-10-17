from __future__ import annotations

import abc
import typing

from .edge import Edge

V = typing.TypeVar("V")
E = typing.TypeVar("E", bound=Edge)


class Graph(abc.ABC, typing.Generic[V, E]):
    @abc.abstractmethod
    def get_vertices(self) -> set[V]:  # pragma: no cover
        pass

    @abc.abstractmethod
    def get_edges(self) -> set[E]:  # pragma: no cover
        pass
