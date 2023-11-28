from dataclasses import dataclass, field
from netex.vehicle_stopping_place_version_structure import VehicleStoppingPlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleStoppingPlace(VehicleStoppingPlaceVersionStructure):
    """
    Designated PLACE within a STOP PLACE for a VEHICLE to stop.

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
