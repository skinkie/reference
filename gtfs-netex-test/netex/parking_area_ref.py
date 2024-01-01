from dataclasses import dataclass
from .parking_area_ref_structure import ParkingAreaRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingAreaRef(ParkingAreaRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
