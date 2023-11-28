from dataclasses import dataclass
from netex.trip_pattern_ref_structure import TripPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TripPatternTripRef(TripPatternRefStructure):
    """
    Reference to a TRIP PATTERN.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
