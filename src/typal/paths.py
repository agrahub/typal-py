from pathlib import Path

from .collections import Seq
from .tuples import Double, Many, Quadruple, Quintuple, Triple

# Basic
OptPath = Path | None
ListOfPaths = list[Path]
SeqOfPaths = Seq[Path]

# Paths tuple
ManyPaths = Many[Path]
ListOfManyPaths = list[ManyPaths]
SeqOfManyPaths = Seq[ManyPaths]

DoublePaths = Double[Path]
ListOfDoublePaths = list[DoublePaths]
SeqOfDoublePaths = Seq[DoublePaths]

TriplePaths = Triple[Path]
ListOfTriplePaths = list[TriplePaths]
SeqOfTriplePaths = Seq[TriplePaths]

QuadruplePaths = Quadruple[Path]
ListOfQuadruplePaths = list[QuadruplePaths]
SeqOfQuadruplePaths = Seq[QuadruplePaths]

QuintuplePaths = Quintuple[Path]
ListOfQuintuplePaths = list[QuintuplePaths]
SeqOfQuintuplePaths = Seq[QuintuplePaths]

# Opt Paths tuple
ManyOptPaths = Many[OptPath]
ListOfManyOptPaths = list[ManyOptPaths]
SeqOfManyOptPaths = Seq[ManyOptPaths]

DoubleOptPaths = Double[OptPath]
ListOfDoubleOptPaths = list[DoubleOptPaths]
SeqOfDoubleOptPaths = Seq[DoubleOptPaths]

TripleOptPaths = Triple[OptPath]
ListOfTripleOptPaths = list[TripleOptPaths]
SeqOfTripleOptPaths = Seq[TripleOptPaths]

QuadrupleOptPaths = Quadruple[OptPath]
ListOfQuadrupleOptPaths = list[QuadrupleOptPaths]
SeqOfQuadrupleOptPaths = Seq[QuadrupleOptPaths]

QuintupleOptPaths = Quintuple[OptPath]
ListOfQuintupleOptPaths = list[QuintupleOptPaths]
SeqOfQuintupleOptPaths = Seq[QuintupleOptPaths]
