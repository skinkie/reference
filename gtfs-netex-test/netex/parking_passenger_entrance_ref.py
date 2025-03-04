from dataclasses import dataclass

from .parking_passenger_entrance_ref_structure import ParkingPassengerEntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ParkingPassengerEntranceRef(ParkingPassengerEntranceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
