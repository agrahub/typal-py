from .collections import Seq
from .tuples import Double, Many, Quadruple, Quintuple, Triple

# Basic
OptBytes = bytes | None
ListOfBytes = list[bytes]
SeqOfBytes = Seq[bytes]

# Bytes tuple
ManyBytes = Many[bytes]
ListOfManyBytes = list[ManyBytes]
SeqOfManyBytes = Seq[ManyBytes]

DoubleBytes = Double[bytes]
ListOfDoubleBytes = list[DoubleBytes]
SeqOfDoubleBytes = Seq[DoubleBytes]

TripleBytes = Triple[bytes]
ListOfTripleBytes = list[TripleBytes]
SeqOfTripleBytes = Seq[TripleBytes]

QuadrupleBytes = Quadruple[bytes]
ListOfQuadrupleBytes = list[QuadrupleBytes]
SeqOfQuadrupleBytes = Seq[QuadrupleBytes]

QuintupleBytes = Quintuple[bytes]
ListOfQuintupleBytes = list[QuintupleBytes]
SeqOfQuintupleBytes = Seq[QuintupleBytes]

# Opt Bytes tuple
ManyOptBytes = Many[OptBytes]
ListOfManyOptBytes = list[ManyOptBytes]
SeqOfManyOptBytes = Seq[ManyOptBytes]

DoubleOptBytes = Double[OptBytes]
ListOfDoubleOptBytes = list[DoubleOptBytes]
SeqOfDoubleOptBytes = Seq[DoubleOptBytes]

TripleOptBytes = Triple[OptBytes]
ListOfTripleOptBytes = list[TripleOptBytes]
SeqOfTripleOptBytes = Seq[TripleOptBytes]

QuadrupleOptBytes = Quadruple[OptBytes]
ListOfQuadrupleOptBytes = list[QuadrupleOptBytes]
SeqOfQuadrupleOptBytes = Seq[QuadrupleOptBytes]

QuintupleOptBytes = Quintuple[OptBytes]
ListOfQuintupleOptBytes = list[QuintupleOptBytes]
SeqOfQuintupleOptBytes = Seq[QuintupleOptBytes]