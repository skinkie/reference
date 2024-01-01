from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EntranceEnumeration(Enum):
    OPENING = "opening"
    OPEN_DOOR = "openDoor"
    DOOR = "door"
    SWING_DOOR = "swingDoor"
    REVOLVING_DOOR = "revolvingDoor"
    AUTOMATIC_DOOR = "automaticDoor"
    TICKET_BARRIER = "ticketBarrier"
    GATE = "gate"
    OTHER = "other"
