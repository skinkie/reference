from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ZoneTopologyEnumeration(Enum):
    OVERLAPPING = "overlapping"
    HONEYCOMB = "honeycomb"
    RING = "ring"
    ANNULAR = "annular"
    NESTED = "nested"
    TILED = "tiled"
    SEQUENCE = "sequence"
    OVERLAPPING_SEQUENCE = "overlappingSequence"
    OTHER = "other"
