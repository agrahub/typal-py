from .collections import Seq
from .tuples import Double, Many, Quadruple, Quintuple, Triple

# Basic
OptInt = int | None
ListOfInts = list[int]
SeqOfInts = Seq[int]

# Ints tuple
ManyInts = Many[int]
ListOfManyInts = list[ManyInts]
SeqOfManyInts = Seq[ManyInts]

DoubleInts = Double[int]
ListOfDoubleInts = list[DoubleInts]
SeqOfDoubleInts = Seq[DoubleInts]

TripleInts = Triple[int]
ListOfTripleInts = list[TripleInts]
SeqOfTripleInts = Seq[TripleInts]

QuadrupleInts = Quadruple[int]
ListOfQuadrupleInts = list[QuadrupleInts]
SeqOfQuadrupleInts = Seq[QuadrupleInts]

QuintupleInts = Quintuple[int]
ListOfQuintupleInts = list[QuintupleInts]
SeqOfQuintupleInts = Seq[QuintupleInts]

# Opt Ints tuple
ManyOptInts = Many[OptInt]
ListOfManyOptInts = list[ManyOptInts]
SeqOfManyOptInts = Seq[ManyOptInts]

DoubleOptInts = Double[OptInt]
ListOfDoubleOptInts = list[DoubleOptInts]
SeqOfDoubleOptInts = Seq[DoubleOptInts]

TripleOptInts = Triple[OptInt]
ListOfTripleOptInts = list[TripleOptInts]
SeqOfTripleOptInts = Seq[TripleOptInts]

QuadrupleOptInts = Quadruple[OptInt]
ListOfQuadrupleOptInts = list[QuadrupleOptInts]
SeqOfQuadrupleOptInts = Seq[QuadrupleOptInts]

QuintupleOptInts = Quintuple[OptInt]
ListOfQuintupleOptInts = list[QuintupleOptInts]
SeqOfQuintupleOptInts = Seq[QuintupleOptInts]