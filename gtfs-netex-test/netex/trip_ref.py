from dataclasses import dataclass
from netex.trip_ref_structure import TripRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TripRef(TripRefStructure):
    """
    Reference to a TRIP.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
