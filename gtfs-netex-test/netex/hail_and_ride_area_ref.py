from dataclasses import dataclass
from netex.hail_and_ride_area_ref_structure import HailAndRideAreaRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class HailAndRideAreaRef(HailAndRideAreaRefStructure):
    """
    Reference to a HAIL AND RIDE AREA.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
