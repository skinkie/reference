from dataclasses import dataclass

from .parking_entrance_ref_structure import ParkingEntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ParkingPassengerEntranceRefStructure(ParkingEntranceRefStructure):
    pass
