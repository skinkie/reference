from dataclasses import dataclass

from .parking_ref_structure import ParkingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ParkingRef(ParkingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
