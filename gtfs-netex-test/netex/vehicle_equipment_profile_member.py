from dataclasses import dataclass

from .vehicle_equipment_profile_member_version_structure import VehicleEquipmentProfileMemberVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleEquipmentProfileMember(VehicleEquipmentProfileMemberVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
