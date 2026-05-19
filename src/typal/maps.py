from typing import Any

from .collections import Map, Seq
from .integers import ListOfInts, SeqOfInts
from .strings import ListOfStrs, SeqOfStrs

# Bytes Key Value
BytesToBytesMap = Map[bytes, bytes]
ListOfBytesToBytesMap = list[BytesToBytesMap]
SeqOfBytesToBytesMap = Seq[BytesToBytesMap]

# Str key
# Any value
StrToAnyMap = Map[str, Any]
ListOfStrToAnyMap = list[StrToAnyMap]
SeqOfStrToAnyMap = Seq[StrToAnyMap]

# Object value
StrToObjectMap = Map[str, object]
ListOfStrToObjectMap = list[StrToObjectMap]
SeqOfStrToObjectMap = Seq[StrToObjectMap]

# Str value
StrToStrMap = Map[str, str]
ListOfStrToStrMap = list[StrToStrMap]
SeqOfStrToStrMap = Seq[StrToStrMap]

# Multi-Str value
StrToListOfStrsMap = Map[str, ListOfStrs]
StrToSeqOfStrsMap = Map[str, SeqOfStrs]

# Int value
StrToIntMap = Map[str, int]
ListOfStrToIntMap = list[StrToIntMap]
SeqOfStrToIntMap = Seq[StrToIntMap]

# Multi-Int value
StrToListOfIntsMap = Map[str, ListOfInts]
StrToSeqOfIntsMap = Map[str, SeqOfInts]

# Int key
# Any value
IntToAnyMap = Map[int, Any]
ListOfIntToAnyMap = list[IntToAnyMap]
SeqOfIntToAnyMap = Seq[IntToAnyMap]

# Object value
IntToObjectMap = Map[int, object]
ListOfIntToObjectMap = list[IntToObjectMap]
SeqOfIntToObjectMap = Seq[IntToObjectMap]

# Str value
IntToStrMap = Map[int, str]
ListOfIntToStrMap = list[IntToStrMap]
SeqOfIntToStrMap = Seq[IntToStrMap]

# Multi-Str value
IntToListOfStrsMap = Map[int, ListOfStrs]
IntToSeqOfStrsMap = Map[int, SeqOfStrs]

# Int value
IntToIntMap = Map[int, int]
ListOfIntToIntMap = list[IntToIntMap]
SeqOfIntToIntMap = Seq[IntToIntMap]

# Multi-Int value
IntToListOfIntsMap = Map[int, ListOfInts]
IntToSeqOfIntsMap = Map[int, SeqOfInts]
