from collections.abc import Iterator
from enum import Enum
from typing import TYPE_CHECKING, ClassVar, Final, Literal, TypeAlias

if TYPE_CHECKING:
    from benchmark import Benchmarked
else:
    # During runtime
    Benchmarked = object()

All: TypeAlias = Final[tuple[str, ...]]
Slots = ClassVar[tuple[str, ...]]
Real: TypeAlias = int | float

Problems: TypeAlias = Iterator[Benchmarked]


class _Sentinel(Enum):
    """
    Single member enum for static typecheckers to validate
    code, this is necessitated due to the fact that
    assigning sentinels to value returned by object()
    causes incorrect type inference.

    See, https://peps.python.org/pep-0661/
    """

    MISSING = object()


MISSING: Literal[_Sentinel.MISSING] = _Sentinel.MISSING