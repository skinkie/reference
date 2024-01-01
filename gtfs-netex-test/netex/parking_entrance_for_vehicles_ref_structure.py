from dataclasses import dataclass
from .parking_entrance_ref_structure import ParkingEntranceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingEntranceForVehiclesRefStructure(ParkingEntranceRefStructure):
    value: RestrictedVar
