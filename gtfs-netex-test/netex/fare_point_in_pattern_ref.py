from dataclasses import dataclass

from .fare_point_in_pattern_ref_structure import FarePointInPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FarePointInPatternRef(FarePointInPatternRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
