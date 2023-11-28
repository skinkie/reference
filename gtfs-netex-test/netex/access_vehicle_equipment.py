from dataclasses import dataclass, field
from netex.access_vehicle_equipment_version_structure import AccessVehicleEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessVehicleEquipment(AccessVehicleEquipmentVersionStructure):
    """
    Specialisation of VEHICLE EQUIPMENT for ACCESS providing information such as
    low floor, ramp, access area dimensions, etc.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
