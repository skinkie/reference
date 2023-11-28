from dataclasses import dataclass, field
from netex.stop_place_entrance_version_structure import StopPlaceEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopPlaceEntrance(StopPlaceEntranceVersionStructure):
    """
    Passenger Entrance to a STOP PLACE.

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
