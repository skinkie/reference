from dataclasses import dataclass, field
from netex.battery_equipment_version_structure import BatteryEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BatteryEquipment(BatteryEquipmentVersionStructure):
    """Specialisation of INSTALLED EQUIPMENT for BATTERY.

    +v1.2.2

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
