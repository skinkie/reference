from dataclasses import dataclass, field
from netex.vehicle_stopping_position_version_structure import VehicleStoppingPositionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleStoppingPosition(VehicleStoppingPositionVersionStructure):
    """
    Designated Position within a VEHICLE STOPPING PLACE for a Vehicle to stop.

    :ivar id: Identifier of VEHICLE STOPPING POSITION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
