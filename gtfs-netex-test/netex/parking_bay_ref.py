from dataclasses import dataclass
from .parking_bay_ref_structure import ParkingBayRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingBayRef(ParkingBayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
