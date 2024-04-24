from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TableTypeEnumeration(Enum):
    NONE = "none"
    FIXED_FLAT = "fixedFlat"
    FOLD_DOWN_FLAT = "foldDownFlat"
    SEAT_BACK_FOLDING = "seatBackFolding"
    ARM_REST_FOLDING = "armRestFolding"
    SEAT_CLIPON = "seatClipon"
    OTHER = "other"
