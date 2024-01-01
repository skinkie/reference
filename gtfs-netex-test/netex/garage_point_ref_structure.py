from dataclasses import dataclass
from .parking_point_ref_structure import ParkingPointRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GaragePointRefStructure(ParkingPointRefStructure):
    value: RestrictedVar
