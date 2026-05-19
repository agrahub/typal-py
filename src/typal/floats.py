from .collections import Seq
from .tuples import Double, Many, Quadruple, Quintuple, Triple

# Basic
OptFloat = float | None
ListOfFloats = list[float]
SeqOfFloats = Seq[float]

# Floats tuple
ManyFloats = Many[float]
ListOfManyFloats = list[ManyFloats]
SeqOfManyFloats = Seq[ManyFloats]

DoubleFloats = Double[float]
ListOfDoubleFloats = list[DoubleFloats]
SeqOfDoubleFloats = Seq[DoubleFloats]

TripleFloats = Triple[float]
ListOfTripleFloats = list[TripleFloats]
SeqOfTripleFloats = Seq[TripleFloats]

QuadrupleFloats = Quadruple[float]
ListOfQuadrupleFloats = list[QuadrupleFloats]
SeqOfQuadrupleFloats = Seq[QuadrupleFloats]

QuintupleFloats = Quintuple[float]
ListOfQuintupleFloats = list[QuintupleFloats]
SeqOfQuintupleFloats = Seq[QuintupleFloats]

# Opt Floats tuple
ManyOptFloats = Many[OptFloat]
ListOfManyOptFloats = list[ManyOptFloats]
SeqOfManyOptFloats = Seq[ManyOptFloats]

DoubleOptFloats = Double[OptFloat]
ListOfDoubleOptFloats = list[DoubleOptFloats]
SeqOfDoubleOptFloats = Seq[DoubleOptFloats]

TripleOptFloats = Triple[OptFloat]
ListOfTripleOptFloats = list[TripleOptFloats]
SeqOfTripleOptFloats = Seq[TripleOptFloats]

QuadrupleOptFloats = Quadruple[OptFloat]
ListOfQuadrupleOptFloats = list[QuadrupleOptFloats]
SeqOfQuadrupleOptFloats = Seq[QuadrupleOptFloats]

QuintupleOptFloats = Quintuple[OptFloat]
ListOfQuintupleOptFloats = list[QuintupleOptFloats]
SeqOfQuintupleOptFloats = Seq[QuintupleOptFloats]