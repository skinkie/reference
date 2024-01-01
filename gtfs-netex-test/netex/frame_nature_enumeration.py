from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FrameNatureEnumeration(Enum):
    PLANNED = "planned"
    OPERATIONAL = "operational"
    CONTINGENCY_PLAN = "contingencyPlan"
    OTHER = "other"
