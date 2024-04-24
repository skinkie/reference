from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SeatContextEnumeration(Enum):
    BY_AISLE_NO_WINDOW = "byAisleNoWindow"
    BY_WINDOW_NO_AISLE = "byWindowNoAisle"
    BY_AISLE_AND_WINDOW = "byAisleAndWindow"
    IN_MIDDLE = "inMiddle"
    UNKNOWN = "unknown"
