from dataclasses import dataclass, field
from netex.vehicle_equipment_profile_version_structure import VehicleEquipmentProfileVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleEquipmentProfile(VehicleEquipmentProfileVersionStructure):
    """Each instantiation of this ENTITY gives the number of items of one TYPE OF
    EQUIPMENT a VEHICLE MODEL should contain for a given PURPOSE OF EQUIPMENT
    PROFILE.

    The set of instantiations for one VEHICLE MODEL and one purpose
    gives one complete 'profile'.

    :ivar id: Identifier of VEHICLE EQUIPMENT PROILE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
