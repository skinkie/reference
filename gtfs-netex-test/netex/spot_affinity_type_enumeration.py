from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SpotAffinityTypeEnumeration(Enum):
    FACE_TO_FACE = "faceToFace"
    SIDE_BY_SIDE = "sideBySide"
    CONTIGUOUS_ROW = "contiguousRow"
    SHARED_TABLE = "sharedTable"
    SEAT_BLOCK = "seatBlock"
    LOWER_BERTHS = "lowerBerths"
    SHARED_COMPARTMENT = "sharedCompartment"
    WHEELCHAIR_COMPANION_SEAT = "wheelchairCompanionSeat"
    OTHER = "other"
