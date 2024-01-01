from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class NecessaryForceEnumeration(Enum):
    NO_FORCE = "noForce"
    LIGHT_FORCE = "lightForce"
    MEDIUM_FORCE = "mediumForce"
    HEAVY_FORCE = "heavyForce"
    UNKNOWN = "unknown"
