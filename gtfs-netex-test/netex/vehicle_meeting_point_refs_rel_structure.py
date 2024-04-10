from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .vehicle_meeting_point_ref import VehicleMeetingPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleMeetingPointRefsRelStructure(OneToManyRelationshipStructure):
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
