from .collections import Seq
from .tuples import Double, Many, Quadruple, Quintuple, Triple

# Basic
OptStr = str | None
ListOfStrs = list[str]
SeqOfStrs = Seq[str]

# Strs tuple
ManyStrs = Many[str]
ListOfManyStrs = list[ManyStrs]
SeqOfManyStrs = Seq[ManyStrs]

DoubleStrs = Double[str]
ListOfDoubleStrs = list[DoubleStrs]
SeqOfDoubleStrs = Seq[DoubleStrs]

TripleStrs = Triple[str]
ListOfTripleStrs = list[TripleStrs]
SeqOfTripleStrs = Seq[TripleStrs]

QuadrupleStrs = Quadruple[str]
ListOfQuadrupleStrs = list[QuadrupleStrs]
SeqOfQuadrupleStrs = Seq[QuadrupleStrs]

QuintupleStrs = Quintuple[str]
ListOfQuintupleStrs = list[QuintupleStrs]
SeqOfQuintupleStrs = Seq[QuintupleStrs]

# Opt Strs tuple
ManyOptStrs = Many[OptStr]
ListOfManyOptStrs = list[ManyOptStrs]
SeqOfManyOptStrs = Seq[ManyOptStrs]

DoubleOptStrs = Double[OptStr]
ListOfDoubleOptStrs = list[DoubleOptStrs]
SeqOfDoubleOptStrs = Seq[DoubleOptStrs]

TripleOptStrs = Triple[OptStr]
ListOfTripleOptStrs = list[TripleOptStrs]
SeqOfTripleOptStrs = Seq[TripleOptStrs]

QuadrupleOptStrs = Quadruple[OptStr]
ListOfQuadrupleOptStrs = list[QuadrupleOptStrs]
SeqOfQuadrupleOptStrs = Seq[QuadrupleOptStrs]

QuintupleOptStrs = Quintuple[OptStr]
ListOfQuintupleOptStrs = list[QuintupleOptStrs]
SeqOfQuintupleOptStrs = Seq[QuintupleOptStrs]
