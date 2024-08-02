from dataclasses import dataclass, field
from typing import Optional

from .equipment_or_system_fault_type_enum import EquipmentOrSystemFaultTypeEnum
from .equipment_or_system_type_enum import EquipmentOrSystemTypeEnum
from .extension_type import ExtensionType
from .traffic_element import TrafficElement

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class EquipmentOrSystemFault(TrafficElement):
    equipment_or_system_fault_type: EquipmentOrSystemFaultTypeEnum = field(
        metadata={
            "name": "equipmentOrSystemFaultType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    faulty_equipment_or_system_type: EquipmentOrSystemTypeEnum = field(
        metadata={
            "name": "faultyEquipmentOrSystemType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    equipment_or_system_fault_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "equipmentOrSystemFaultExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
