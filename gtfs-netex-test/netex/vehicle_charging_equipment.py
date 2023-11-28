from dataclasses import dataclass, field
from netex.vehicle_charging_equipment_version_structure import VehicleChargingEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleChargingEquipment(VehicleChargingEquipmentVersionStructure):
    """
    Specialisation of PLACE EQUIPMENT for vehicle charging.

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
