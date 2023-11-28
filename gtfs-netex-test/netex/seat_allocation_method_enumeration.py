from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SeatAllocationMethodEnumeration(Enum):
    """
    Allowed values for Seat Alllocation Method.

    :cvar AUTO_ASSIGNED: A seat will be assigned automatically by an
        algorithm.
    :cvar SEAT_MAP: The passenger may choose a specific seat from the
        available seats.
    :cvar OPEN_SEATING: It is not possible to  reserve a specific seat.
    """
    AUTO_ASSIGNED = "autoAssigned"
    SEAT_MAP = "seatMap"
    OPEN_SEATING = "openSeating"
