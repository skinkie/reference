from dataclasses import dataclass, field
from typing import Optional

from .comparison_operator_enum import ComparisonOperatorEnum
from .extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class HeaviestAxleWeightCharacteristic:
    comparison_operator: ComparisonOperatorEnum = field(
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    heaviest_axle_weight: float = field(
        metadata={
            "name": "heaviestAxleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    heaviest_axle_weight_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "heaviestAxleWeightCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
