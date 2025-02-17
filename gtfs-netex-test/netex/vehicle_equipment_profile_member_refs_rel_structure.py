from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .vehicle_equipment_profile_member_ref import VehicleEquipmentProfileMemberRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleEquipmentProfileMemberRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "vehicleEquipmentProfileMemberRefs_RelStructure"

    vehicle_equipment_profile_member_ref: list[VehicleEquipmentProfileMemberRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleEquipmentProfileMemberRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
