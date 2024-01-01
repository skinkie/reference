from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MeetingUsageEnumeration(Enum):
    PICK_UP = "pickUp"
    SET_DOWN = "setDown"
    ALL = "all"
