# typal

A lightweight collection of reusable typing utilities for modern Python.

## Overview

typal provides small, composable building blocks for Python type annotations.

It avoids type explosion and focuses on clarity, reuse, and native typing features.

---

## Features

- Optional type helpers (`Opt[T]`)
- Functional type aliases (`Mapper`, `Predicate`, `Action`)
- Collection shortcuts (`Seq[T]`, `List[T]`)
- Common type unions (`StrOrInt`, `PathOrStr`, etc.)
- Enum-aware type utilities
- Clean separation of typing concerns

---

## Installation

Using uv:

```bash
uv add typal
```

Or pip:

```bash
pip install typal
```

## Usage

### Optionals
```python
from typal.optionals import Opt

value: Opt[int] = None
```

### Collections
```python
from typal.collections import Seq

def process(items: Seq[str]) -> None:
    ...
```

### Functional types
```python
from typal.functional import Mapper, Predicate, Action

def transform(x: int) -> str:
    return str(x)

m: Mapper[int, str] = transform
```

### Unions
```python
from typal.unions import StrOrInt, PathOrStr

def load(path: PathOrStr) -> StrOrInt:
    ...
```

### Tuples
```python
from typal.tuples import Pair, Triple

Point = Pair[float]
RGB = Triple[int]
```

## Design Philosophy

typal follows these principles:

- Prefer native Python typing (`|`, `list[T]`, `dict[K, V]`)
- Avoid combinatorial type explosion
- Provide reusable abstractions, not exhaustive aliases
- Keep the API small, predictable, and composable

## Non-goals

typal does NOT aim to:

- Replace Python's built-in typing system
- Provide exhaustive pre-generated type variants
- Introduce framework-specific abstractions
- Replace domain models
