from dataclasses import dataclass, field
from netex.parking_point_version_structure import ParkingPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingPoint(ParkingPointVersionStructure):
    """A TIMING POINT where vehicles may stay unattended for a long time.

    A vehicle's return to park at a PARKING POINT marks the end of a
    BLOCK.

    :ivar id: Identifier of a PARKING POINT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
