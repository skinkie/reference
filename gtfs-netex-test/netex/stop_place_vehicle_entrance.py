from dataclasses import dataclass, field
from netex.stop_place_vehicle_entrance_version_structure import StopPlaceVehicleEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopPlaceVehicleEntrance(StopPlaceVehicleEntranceVersionStructure):
    """A physical entrance or exit to/from a SITE for a VEHICLE.

    May be a door, barrier, gate or other recognizable point of access.

    :ivar id: Identifier of STOP PLACE ENTRANCE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
