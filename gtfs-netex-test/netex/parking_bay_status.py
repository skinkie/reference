from dataclasses import dataclass, field
from netex.parking_bay_status_value_structure import ParkingBayStatusValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingBayStatus(ParkingBayStatusValueStructure):
    """A categorisation of the  availability of the parking spot, such as being
    temporarily closed, unavailable, available.

    +v1.2.2

    :ivar id: Identifier of PARKING BAY STATUS.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
