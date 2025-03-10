from dataclasses import dataclass

from .parking_point_ref_structure import ParkingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ParkingPointRef(ParkingPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
