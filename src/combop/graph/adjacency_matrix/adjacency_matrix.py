from __future__ import annotations

import abc
import typing

from ..edge import Edge

V = typing.TypeVar("V")
E = typing.TypeVar("E", bound=Edge)


class AdjacencyMatrix(abc.ABC, typing.Generic[V, E]):
    pass
