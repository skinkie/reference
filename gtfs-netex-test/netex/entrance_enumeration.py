from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EntranceEnumeration(Enum):
    """
    Allowed values for doors status.
    """
    OPENING = "opening"
    OPEN_DOOR = "openDoor"
    DOOR = "door"
    SWING_DOOR = "swingDoor"
    REVOLVING_DOOR = "revolvingDoor"
    AUTOMATIC_DOOR = "automaticDoor"
    TICKET_BARRIER = "ticketBarrier"
    GATE = "gate"
    OTHER = "other"
