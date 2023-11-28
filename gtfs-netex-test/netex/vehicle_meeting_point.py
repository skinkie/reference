from dataclasses import dataclass, field
from netex.vehicle_meeting_point_version_structure import VehicleMeetingPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingPoint(VehicleMeetingPointVersionStructure):
    """A POINT where passengers can board or alight from vehicles.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
