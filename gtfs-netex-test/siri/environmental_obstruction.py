from dataclasses import dataclass, field
from typing import Optional

from .environmental_obstruction_type_enum import EnvironmentalObstructionTypeEnum
from .extension_type import ExtensionType
from .obstruction import Obstruction

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class EnvironmentalObstruction(Obstruction):
    depth: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    environmental_obstruction_type: EnvironmentalObstructionTypeEnum = field(
        metadata={
            "name": "environmentalObstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    environmental_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "environmentalObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
