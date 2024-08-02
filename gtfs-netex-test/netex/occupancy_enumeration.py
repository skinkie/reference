from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class OccupancyEnumeration(Enum):
    UNKNOWN = "unknown"
    EMPTY = "empty"
    MANY_SEATS_AVAILABLE = "manySeatsAvailable"
    FEW_SEATS_AVAILABLE = "fewSeatsAvailable"
    STANDING_ROOM_ONLY = "standingRoomOnly"
    CRUSHED_STANDING_ROOM_ONLY = "crushedStandingRoomOnly"
    FULL = "full"
    NOT_ACCEPTING_PASSENGERS = "notAcceptingPassengers"
    UNDEFINED = "undefined"
    SEATS_AVAILABLE = "seatsAvailable"
    STANDING_AVAILABLE = "standingAvailable"
