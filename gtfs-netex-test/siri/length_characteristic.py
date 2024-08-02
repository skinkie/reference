from dataclasses import dataclass, field
from typing import Optional

from .comparison_operator_enum import ComparisonOperatorEnum
from .extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class LengthCharacteristic:
    comparison_operator: ComparisonOperatorEnum = field(
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    vehicle_length: float = field(
        metadata={
            "name": "vehicleLength",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    length_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "lengthCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
