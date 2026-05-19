from enum import IntEnum, StrEnum

from .collections import Seq

# Int Enum
OptIntEnum = IntEnum | None
ListOfIntEnums = list[IntEnum]
SeqOfIntEnums = Seq[IntEnum]

# Str Enum
OptStrEnum = StrEnum | None
ListOfStrEnums = list[StrEnum]
SeqOfStrEnums = Seq[StrEnum]
