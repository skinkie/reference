from dataclasses import dataclass, field
from typing import Optional
from netex.fuel_type_enumeration import FuelTypeEnumeration
from netex.place_equipment_version_structure import PlaceEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RefuellingEquipmentVersionStructure(PlaceEquipmentVersionStructure):
    """
    Type for a REFUELLING EQUIPMENT.

    :ivar fuel_type: The type of fuel used by a vehicle of the type.
    """
    class Meta:
        name = "RefuellingEquipment_VersionStructure"

    fuel_type: Optional[FuelTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "FuelType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
