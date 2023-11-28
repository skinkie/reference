from dataclasses import dataclass, field
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.vehicle_meeting_point_ref import VehicleMeetingPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingPointRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of VEHICLE MEETING POINTs.
    """
    class Meta:
        name = "vehicleMeetingPointRefs_RelStructure"

    vehicle_meeting_point_ref: VehicleMeetingPointRef = field(
        metadata={
            "name": "VehicleMeetingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
