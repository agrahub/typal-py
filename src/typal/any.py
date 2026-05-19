from typing import Any

from .collections import Seq

ListOfAny = list[Any]
SeqOfAny = Seq[Any]

# Any tuple
ManyAny = tuple[Any, ...]
ListOfManyAny = list[ManyAny]
SeqOfManyAny = Seq[ManyAny]

DoubleAny = tuple[Any, Any]
ListOfDoubleAny = list[DoubleAny]
SeqOfDoubleAny = Seq[DoubleAny]

TripleAny = tuple[Any, Any, Any]
ListOfTripleAny = list[TripleAny]
SeqOfTripleAny = Seq[TripleAny]

QuadrupleAny = tuple[Any, Any, Any, Any]
ListOfQuadrupleAny = list[QuadrupleAny]
SeqOfQuadrupleAny = Seq[QuadrupleAny]

QuintupleAny = tuple[Any, Any, Any, Any, Any]
ListOfQuintupleAny = list[QuintupleAny]
SeqOfQuintupleAny = Seq[QuintupleAny]
