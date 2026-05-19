from typal.collections import Seq
from typal.tuples import Double, Triple
from typal.unions import IntOrStr


def test_seq_alias():
    x: Seq[int] = [1, 2, 3]
    assert len(x) == 3


def test_union_alias():
    x: IntOrStr = "hello"
    y: IntOrStr = 123
    assert isinstance(x, str)
    assert isinstance(y, int)


def test_tuple_alias():
    p: Double[int] = (1, 2)
    t: Triple[str] = ("a", "b", "c")
    assert p[0] == 1
    assert t[2] == "c"
