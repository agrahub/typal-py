from enum import IntEnum, StrEnum
from pathlib import Path
from uuid import UUID

from .any import ListOfAny, SeqOfAny
from .dicts import StrToAnyDict
from .enums import ListOfIntEnums, ListOfStrEnums, SeqOfIntEnums, SeqOfStrEnums
from .floats import ListOfFloats, SeqOfFloats
from .integers import ListOfInts, SeqOfInts
from .maps import StrToAnyMap
from .strings import ListOfStrs, SeqOfStrs
from .uuids import ListOfUUIDs, SeqOfUUIDs

# Bytes x Memoryview
BytesOrMemoryview = bytes | memoryview

# Path x Str
PathOrStr = Path | str

# Bytes x Str
BytesOrStr = bytes | str

# Float x Int
FloatOrInt = float | int
ListOfFloatsOrInts = ListOfFloats | ListOfInts
SeqOfFloatsOrInts = SeqOfFloats | SeqOfInts

# Int x Str
IntOrStr = int | str
ListOfIntsOrStrs = ListOfInts | ListOfStrs
SeqOfIntsOrStrs = SeqOfInts | SeqOfStrs

# Int x IntEnum
IntOrIntEnum = int | IntEnum
ListOfIntsOrIntEnums = ListOfInts | ListOfIntEnums
SeqOfIntsOrIntEnums = SeqOfInts | SeqOfIntEnums

# Int x StrEnum
IntOrStrEnum = int | StrEnum
ListOfIntsOrStrEnums = ListOfInts | ListOfStrEnums
SeqOfIntsOrStrEnums = SeqOfInts | SeqOfStrEnums

# Int x UUID
IntOrUUID = int | UUID
ListOfIntsOrUUIDs = ListOfInts | ListOfUUIDs
SeqOfIntsOrUUIDs = SeqOfInts | SeqOfUUIDs

# Str x IntEnum
StrOrIntEnum = str | IntEnum
ListOfStrsOrIntEnums = ListOfStrs | ListOfIntEnums
SeqOfStrsOrIntEnums = SeqOfStrs | SeqOfIntEnums

# Str x StrEnum
StrOrStrEnum = str | StrEnum
ListOfStrsOrStrEnums = ListOfStrs | ListOfStrEnums
SeqOfStrsOrStrEnums = SeqOfStrs | SeqOfStrEnums

# Str x UUID
StrOrUUID = str | UUID
ListOfStrsOrUUIDs = ListOfStrs | ListOfUUIDs
SeqOfStrsOrUUIDs = SeqOfStrs | SeqOfUUIDs

# Any
ListOfAnyOrStrToAnyDict = ListOfAny | StrToAnyDict
ListOfAnyOrStrToAnyMap = ListOfAny | StrToAnyMap
SeqOfAnyOrStrToAnyDict = SeqOfAny | StrToAnyDict
SeqOfAnyOrStrToAnyMap = SeqOfAny | StrToAnyMap
