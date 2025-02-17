from dataclasses import dataclass

from .parking_bay_ref_structure import ParkingBayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ParkingBayRef(ParkingBayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
