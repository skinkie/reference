from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StopUseConstraintEnumeration(Enum):
    ARRIVING = "arriving"
    DEPARTING = "departing"
    PASSING_THROUGH = "passingThrough"
