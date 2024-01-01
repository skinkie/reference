from dataclasses import dataclass
from .parking_version_structure import ParkingVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Parking(ParkingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
