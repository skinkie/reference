from dataclasses import dataclass, field
from netex.vehicle_meeting_link_version_structure import VehicleMeetingLinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingLink(VehicleMeetingLinkVersionStructure):
    """A LINK between an ordered pair of STOP POINTs.

    VEHICLE MEETING LINKs are directional - there will be separate links for each direction of a route.  +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
