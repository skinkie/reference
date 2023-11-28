from dataclasses import dataclass
from netex.fare_point_in_pattern_ref_structure import FarePointInPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FarePointInPatternRef(FarePointInPatternRefStructure):
    """
    Reference to a FARE POINT IN JOURNEY PATTERN.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
