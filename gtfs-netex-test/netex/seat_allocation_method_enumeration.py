from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SeatAllocationMethodEnumeration(Enum):
    AUTO_ASSIGNED = "autoAssigned"
    SEAT_MAP = "seatMap"
    OPEN_SEATING = "openSeating"
