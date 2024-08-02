from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .network_management import NetworkManagement
from .winter_equipment_management_type_enum import WinterEquipmentManagementTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class WinterDrivingManagement(NetworkManagement):
    winter_equipment_management_type: WinterEquipmentManagementTypeEnum = field(
        metadata={
            "name": "winterEquipmentManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    winter_driving_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "winterDrivingManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
