from .collections import Map, Seq
from .tuples import Double, Many, Quadruple, Quintuple, Triple

# Basic
Primitive = bool | float | int | str
OptPrimitive = Primitive | None
ListOfPrimitives = list[Primitive]
PrimitiveOrListOfPrimitives = Primitive | ListOfPrimitives
SeqOfPrimitives = Seq[Primitive]
PrimitiveOrSeqOfPrimitives = Primitive | SeqOfPrimitives


StrPrimitiveTuple = tuple[str, Primitive]
ListOfStrPrimitiveTuples = list[StrPrimitiveTuple]
SeqOfStrPrimitiveTuples = Seq[StrPrimitiveTuple]
ManyStrPrimitiveTuples = tuple[StrPrimitiveTuple, ...]
StrToPrimitiveOrSeqOfPrimitivesDict = dict[str, PrimitiveOrSeqOfPrimitives]
StrToPrimitiveOrSeqOfPrimitivesMap = Map[str, PrimitiveOrSeqOfPrimitives]


StrOptPrimitiveTuple = tuple[str, OptPrimitive]
ListOfStrOptPrimitiveTuples = list[StrOptPrimitiveTuple]
SeqOfStrOptPrimitiveTuples = Seq[StrOptPrimitiveTuple]
ManyStrOptPrimitiveTuples = tuple[StrOptPrimitiveTuple, ...]
StrToOptPrimitiveOrSeqOfPrimitivesDict = dict[str, PrimitiveOrSeqOfPrimitives | None]
StrToOptPrimitiveOrSeqOfPrimitivesMap = Map[str, PrimitiveOrSeqOfPrimitives | None]

# Primitives tuple
ManyPrimitives = Many[Primitive]
ListOfManyPrimitives = list[ManyPrimitives]
SeqOfManyPrimitives = Seq[ManyPrimitives]

DoublePrimitives = Double[Primitive]
ListOfDoublePrimitives = list[DoublePrimitives]
SeqOfDoublePrimitives = Seq[DoublePrimitives]

TriplePrimitives = Triple[Primitive]
ListOfTriplePrimitives = list[TriplePrimitives]
SeqOfTriplePrimitives = Seq[TriplePrimitives]

QuadruplePrimitives = Quadruple[Primitive]
ListOfQuadruplePrimitives = list[QuadruplePrimitives]
SeqOfQuadruplePrimitives = Seq[QuadruplePrimitives]

QuintuplePrimitives = Quintuple[Primitive]
ListOfQuintuplePrimitives = list[QuintuplePrimitives]
SeqOfQuintuplePrimitives = Seq[QuintuplePrimitives]