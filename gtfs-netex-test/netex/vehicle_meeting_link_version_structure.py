from dataclasses import dataclass, field
from netex.link_version_structure import LinkVersionStructure
from netex.vehicle_meeting_point_ref_structure import VehicleMeetingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingLinkVersionStructure(LinkVersionStructure):
    """
    Type for VEHICLE MEETING LINK.

    :ivar from_point_ref: Identifier of VEHICLE MEETING POINT from which
        Link starts.
    :ivar to_point_ref: Identifier of VEHICLE MEETING POINT at which
        Link ends.
    """
    class Meta:
        name = "VehicleMeetingLink_VersionStructure"

    from_point_ref: VehicleMeetingPointRefStructure = field(
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_point_ref: VehicleMeetingPointRefStructure = field(
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
