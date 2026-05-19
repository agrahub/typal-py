from typing import Any

from .collections import Seq
from .integers import ListOfInts, SeqOfInts
from .strings import ListOfStrs, SeqOfStrs

# Bytes Key Value
BytesToBytesDict = dict[bytes, bytes]
ListOfBytesToBytesDict = list[BytesToBytesDict]
SeqOfBytesToBytesDict = Seq[BytesToBytesDict]

# Str key
# Any value
StrToAnyDict = dict[str, Any]
ListOfStrToAnyDict = list[StrToAnyDict]
SeqOfStrToAnyDict = Seq[StrToAnyDict]

# Object value
StrToObjectDict = dict[str, object]
ListOfStrToObjectDict = list[StrToObjectDict]
SeqOfStrToObjectDict = Seq[StrToObjectDict]

# Str value
StrToStrDict = dict[str, str]
ListOfStrToStrDict = list[StrToStrDict]
SeqOfStrToStrDict = Seq[StrToStrDict]

# Multi-Str value
StrToListOfStrsDict = dict[str, ListOfStrs]
StrToSeqOfStrsDict = dict[str, SeqOfStrs]

# Int value
StrToIntDict = dict[str, int]
ListOfStrToIntDict = list[StrToIntDict]
SeqOfStrToIntDict = Seq[StrToIntDict]

# Multi-Int value
StrToListOfIntsDict = dict[str, ListOfInts]
StrToSeqOfIntsDict = dict[str, SeqOfInts]

# Int key
# Any value
IntToAnyDict = dict[int, Any]
ListOfIntToAnyDict = list[IntToAnyDict]
SeqOfIntToAnyDict = Seq[IntToAnyDict]

# Object value
IntToObjectDict = dict[int, object]
ListOfIntToObjectDict = list[IntToObjectDict]
SeqOfIntToObjectDict = Seq[IntToObjectDict]

# Str value
IntToStrDict = dict[int, str]
ListOfIntToStrDict = list[IntToStrDict]
SeqOfIntToStrDict = Seq[IntToStrDict]

# Multi-Str value
IntToListOfStrsDict = dict[int, ListOfStrs]
IntToSeqOfStrsDict = dict[int, SeqOfStrs]

# Int value
IntToIntDict = dict[int, int]
ListOfIntToIntDict = list[IntToIntDict]
SeqOfIntToIntDict = Seq[IntToIntDict]

# Multi-Int value
IntToListOfIntsDict = dict[int, ListOfInts]
IntToSeqOfIntsDict = dict[int, SeqOfInts]
