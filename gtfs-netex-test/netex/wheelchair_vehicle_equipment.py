from dataclasses import dataclass, field
from netex.wheelchair_vehicle_equipment_version_structure import WheelchairVehicleEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class WheelchairVehicleEquipment(WheelchairVehicleEquipmentVersionStructure):
    """
    Specialisation of VEHICLE EQUIPMENT for Wheel chair accessibility on board a
    VEHICLE providing information such as the number of wheel chair areas and the
    access dimensions.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
