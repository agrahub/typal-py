from typing import Literal

from .collections import Seq
from .tuples import Double, Many, Quadruple, Quintuple, Triple

# Basic
LiteralFalse = Literal[False]
LiteralTrue = Literal[True]
OptBool = bool | None
ListOfBools = list[bool]
SeqOfBools = Seq[bool]

# Bools tuple
ManyBools = Many[bool]
ListOfManyBools = list[ManyBools]
SeqOfManyBools = Seq[ManyBools]

DoubleBools = Double[bool]
ListOfDoubleBools = list[DoubleBools]
SeqOfDoubleBools = Seq[DoubleBools]

TripleBools = Triple[bool]
ListOfTripleBools = list[TripleBools]
SeqOfTripleBools = Seq[TripleBools]

QuadrupleBools = Quadruple[bool]
ListOfQuadrupleBools = list[QuadrupleBools]
SeqOfQuadrupleBools = Seq[QuadrupleBools]

QuintupleBools = Quintuple[bool]
ListOfQuintupleBools = list[QuintupleBools]
SeqOfQuintupleBools = Seq[QuintupleBools]

# Opt Bools tuple
ManyOptBools = Many[OptBool]
ListOfManyOptBools = list[ManyOptBools]
SeqOfManyOptBools = Seq[ManyOptBools]

DoubleOptBools = Double[OptBool]
ListOfDoubleOptBools = list[DoubleOptBools]
SeqOfDoubleOptBools = Seq[DoubleOptBools]

TripleOptBools = Triple[OptBool]
ListOfTripleOptBools = list[TripleOptBools]
SeqOfTripleOptBools = Seq[TripleOptBools]

QuadrupleOptBools = Quadruple[OptBool]
ListOfQuadrupleOptBools = list[QuadrupleOptBools]
SeqOfQuadrupleOptBools = Seq[QuadrupleOptBools]

QuintupleOptBools = Quintuple[OptBool]
ListOfQuintupleOptBools = list[QuintupleOptBools]
SeqOfQuintupleOptBools = Seq[QuintupleOptBools]