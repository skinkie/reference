from dataclasses import dataclass
from .parking_passenger_entrance_ref_structure import (
    ParkingPassengerEntranceRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingPassengerEntranceRef(ParkingPassengerEntranceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: RestrictedVar
