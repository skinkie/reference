from dataclasses import dataclass, field
from netex.parking_passenger_entrance_version_structure import ParkingPassengerEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingPassengerEntrance(ParkingPassengerEntranceVersionStructure):
    """
    Designated Passenger ENTRANCE within a PARKING.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
