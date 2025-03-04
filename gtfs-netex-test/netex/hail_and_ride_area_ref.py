from dataclasses import dataclass

from .hail_and_ride_area_ref_structure import HailAndRideAreaRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class HailAndRideAreaRef(HailAndRideAreaRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
