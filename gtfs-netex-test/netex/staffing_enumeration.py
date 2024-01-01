from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StaffingEnumeration(Enum):
    FULL_TIME = "fullTime"
    PART_TIME = "partTime"
    UNMANNED = "unmanned"
