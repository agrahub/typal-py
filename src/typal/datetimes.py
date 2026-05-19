from datetime import datetime

from .collections import Seq
from .tuples import Double, Many, Quadruple, Quintuple, Triple

# Basic
OptDatetime = datetime | None
ListOfDatetimes = list[datetime]
SeqOfDatetimes = Seq[datetime]

# Datetimes tuple
ManyDatetimes = Many[datetime]
ListOfManyDatetimes = list[ManyDatetimes]
SeqOfManyDatetimes = Seq[ManyDatetimes]

DoubleDatetimes = Double[datetime]
ListOfDoubleDatetimes = list[DoubleDatetimes]
SeqOfDoubleDatetimes = Seq[DoubleDatetimes]

TripleDatetimes = Triple[datetime]
ListOfTripleDatetimes = list[TripleDatetimes]
SeqOfTripleDatetimes = Seq[TripleDatetimes]

QuadrupleDatetimes = Quadruple[datetime]
ListOfQuadrupleDatetimes = list[QuadrupleDatetimes]
SeqOfQuadrupleDatetimes = Seq[QuadrupleDatetimes]

QuintupleDatetimes = Quintuple[datetime]
ListOfQuintupleDatetimes = list[QuintupleDatetimes]
SeqOfQuintupleDatetimes = Seq[QuintupleDatetimes]

# Opt Datetimes tuple
ManyOptDatetimes = Many[OptDatetime]
ListOfManyOptDatetimes = list[ManyOptDatetimes]
SeqOfManyOptDatetimes = Seq[ManyOptDatetimes]

DoubleOptDatetimes = Double[OptDatetime]
ListOfDoubleOptDatetimes = list[DoubleOptDatetimes]
SeqOfDoubleOptDatetimes = Seq[DoubleOptDatetimes]

TripleOptDatetimes = Triple[OptDatetime]
ListOfTripleOptDatetimes = list[TripleOptDatetimes]
SeqOfTripleOptDatetimes = Seq[TripleOptDatetimes]

QuadrupleOptDatetimes = Quadruple[OptDatetime]
ListOfQuadrupleOptDatetimes = list[QuadrupleOptDatetimes]
SeqOfQuadrupleOptDatetimes = Seq[QuadrupleOptDatetimes]

QuintupleOptDatetimes = Quintuple[OptDatetime]
ListOfQuintupleOptDatetimes = list[QuintupleOptDatetimes]
SeqOfQuintupleOptDatetimes = Seq[QuintupleOptDatetimes]
