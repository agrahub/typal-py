from typal.functionals import Action, Mapper, Predicate
from typal.integers import ListOfInts


def test_mapper():
    def f(x: int) -> str:
        return str(x)

    m: Mapper[int, str] = f
    assert m(1) == "1"


def test_predicate():
    def f(x: int) -> bool:
        return x > 0

    p: Predicate[int] = f
    assert p(1) is True


def test_action():
    result: ListOfInts = []

    def f(x: int) -> None:
        result.append(x)

    a: Action[int] = f
    a(10)

    assert result == [10]
