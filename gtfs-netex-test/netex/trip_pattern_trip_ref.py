from dataclasses import dataclass
from .trip_pattern_ref_structure import TripPatternRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TripPatternTripRef(TripPatternRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
