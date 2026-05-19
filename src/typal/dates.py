from datetime import date

from .collections import Seq
from .tuples import Double, Many, Quadruple, Quintuple, Triple

# Basic
OptDate = date | None
ListOfDates = list[date]
SeqOfDates = Seq[date]

# Dates tuple
ManyDates = Many[date]
ListOfManyDates = list[ManyDates]
SeqOfManyDates = Seq[ManyDates]

DoubleDates = Double[date]
ListOfDoubleDates = list[DoubleDates]
SeqOfDoubleDates = Seq[DoubleDates]

TripleDates = Triple[date]
ListOfTripleDates = list[TripleDates]
SeqOfTripleDates = Seq[TripleDates]

QuadrupleDates = Quadruple[date]
ListOfQuadrupleDates = list[QuadrupleDates]
SeqOfQuadrupleDates = Seq[QuadrupleDates]

QuintupleDates = Quintuple[date]
ListOfQuintupleDates = list[QuintupleDates]
SeqOfQuintupleDates = Seq[QuintupleDates]

# Opt Dates tuple
ManyOptDates = Many[OptDate]
ListOfManyOptDates = list[ManyOptDates]
SeqOfManyOptDates = Seq[ManyOptDates]

DoubleOptDates = Double[OptDate]
ListOfDoubleOptDates = list[DoubleOptDates]
SeqOfDoubleOptDates = Seq[DoubleOptDates]

TripleOptDates = Triple[OptDate]
ListOfTripleOptDates = list[TripleOptDates]
SeqOfTripleOptDates = Seq[TripleOptDates]

QuadrupleOptDates = Quadruple[OptDate]
ListOfQuadrupleOptDates = list[QuadrupleOptDates]
SeqOfQuadrupleOptDates = Seq[QuadrupleOptDates]

QuintupleOptDates = Quintuple[OptDate]
ListOfQuintupleOptDates = list[QuintupleOptDates]
SeqOfQuintupleOptDates = Seq[QuintupleOptDates]
