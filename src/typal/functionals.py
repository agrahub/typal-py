from collections.abc import Callable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")

# ParamSpec-based (general functions)
Action = Callable[P, None]
Function = Callable[P, R]
Predicate = Callable[P, bool]

# Simple transformation (semantic meaning preserved)
type Mapper[A, B] = Function[[A], B]
