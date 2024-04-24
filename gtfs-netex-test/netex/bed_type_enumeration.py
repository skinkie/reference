from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BedTypeEnumeration(Enum):
    SINGLE_BED = "singleBed"
    DOUBLE_BED = "doubleBed"
    BED_FOR_CHILD = "bedForChild"
    COT = "cot"
    BOTTOM_BUNK = "bottomBunk"
    MIDDLE_BUNK = "middleBunk"
    TOP_BUNK = "topBunk"
    HAMMOCK = "hammock"
    OTHER = "other"
