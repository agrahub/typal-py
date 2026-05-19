from uuid import UUID

from .collections import Seq
from .tuples import Double, Many, Quadruple, Quintuple, Triple

# Basic
OptUUID = UUID | None
ListOfUUIDs = list[UUID]
SeqOfUUIDs = Seq[UUID]

# UUIDs tuple
ManyUUIDs = Many[UUID]
ListOfManyUUIDs = list[ManyUUIDs]
SeqOfManyUUIDs = Seq[ManyUUIDs]

DoubleUUIDs = Double[UUID]
ListOfDoubleUUIDs = list[DoubleUUIDs]
SeqOfDoubleUUIDs = Seq[DoubleUUIDs]

TripleUUIDs = Triple[UUID]
ListOfTripleUUIDs = list[TripleUUIDs]
SeqOfTripleUUIDs = Seq[TripleUUIDs]

QuadrupleUUIDs = Quadruple[UUID]
ListOfQuadrupleUUIDs = list[QuadrupleUUIDs]
SeqOfQuadrupleUUIDs = Seq[QuadrupleUUIDs]

QuintupleUUIDs = Quintuple[UUID]
ListOfQuintupleUUIDs = list[QuintupleUUIDs]
SeqOfQuintupleUUIDs = Seq[QuintupleUUIDs]

# Opt UUIDs tuple
ManyOptUUIDs = Many[OptUUID]
ListOfManyOptUUIDs = list[ManyOptUUIDs]
SeqOfManyOptUUIDs = Seq[ManyOptUUIDs]

DoubleOptUUIDs = Double[OptUUID]
ListOfDoubleOptUUIDs = list[DoubleOptUUIDs]
SeqOfDoubleOptUUIDs = Seq[DoubleOptUUIDs]

TripleOptUUIDs = Triple[OptUUID]
ListOfTripleOptUUIDs = list[TripleOptUUIDs]
SeqOfTripleOptUUIDs = Seq[TripleOptUUIDs]

QuadrupleOptUUIDs = Quadruple[OptUUID]
ListOfQuadrupleOptUUIDs = list[QuadrupleOptUUIDs]
SeqOfQuadrupleOptUUIDs = Seq[QuadrupleOptUUIDs]

QuintupleOptUUIDs = Quintuple[OptUUID]
ListOfQuintupleOptUUIDs = list[QuintupleOptUUIDs]
SeqOfQuintupleOptUUIDs = Seq[QuintupleOptUUIDs]
