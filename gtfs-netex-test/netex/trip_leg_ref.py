from dataclasses import dataclass
from netex.trip_leg_ref_structure import TripLegRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TripLegRef(TripLegRefStructure):
    """
    Reference to a TRIP LEG.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
