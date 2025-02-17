from dataclasses import dataclass

from .trip_ref_structure import TripRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TripRef(TripRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
