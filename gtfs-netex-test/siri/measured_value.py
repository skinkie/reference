from dataclasses import dataclass, field
from typing import Optional

from .basic_data_value import BasicDataValue
from .extension_type import ExtensionType
from .location_characteristics_override import LocationCharacteristicsOverride
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class MeasuredValue:
    measurement_equipment_type_used: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "measurementEquipmentTypeUsed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    location_characteristics_override: Optional[LocationCharacteristicsOverride] = field(
        default=None,
        metadata={
            "name": "locationCharacteristicsOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    basic_data_value: BasicDataValue = field(
        metadata={
            "name": "basicDataValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    measured_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measuredValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
