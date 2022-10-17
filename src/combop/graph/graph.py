from __future__ import annotations

import abc
import typing

from .edge import Edge

V = typing.TypeVar("V")
E = typing.TypeVar("E", bound=Edge)


class Graph(abc.ABC, typing.Generic[V, E]):
    @property
    @abc.abstractmethod
    def vertices(self) -> set[V]:  # pragma: no cover
        pass

    @property
    @abc.abstractmethod
    def edges(self) -> set[E]:  # pragma: no cover
        pass
