from dataclasses import dataclass, field
from netex.vehicle_pooling_meeting_place_version_structure import VehiclePoolingMeetingPlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingMeetingPlace(VehiclePoolingMeetingPlaceVersionStructure):
    """A place where  vehicles/passengers meet to change mode of transportation,
    for boarding, alighting, pick-up, drop-off, etc.

    +v1.2.2

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
