from dataclasses import dataclass

from .fare_point_in_pattern_versioned_child_structure import FarePointInPatternVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FarePointInPattern(FarePointInPatternVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
