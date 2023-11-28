from dataclasses import dataclass, field
from netex.charging_equipment_profile_version_structure import ChargingEquipmentProfileVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ChargingEquipmentProfile(ChargingEquipmentProfileVersionStructure):
    """
    Specialisation of VEHICLE EQUIPMENT PROFILE describing vehicle charging
    features.

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
