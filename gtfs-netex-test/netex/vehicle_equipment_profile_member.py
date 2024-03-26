from dataclasses import dataclass

from .vehicle_equipment_profile_member_versioned_child_structure import (
    VehicleEquipmentProfileMemberVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleEquipmentProfileMember(
    VehicleEquipmentProfileMemberVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
