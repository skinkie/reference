from dataclasses import dataclass

from .parking_point_version_structure import ParkingPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ParkingPoint(ParkingPointVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
