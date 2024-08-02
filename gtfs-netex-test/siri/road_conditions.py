from dataclasses import dataclass, field
from typing import Optional

from .conditions import Conditions
from .extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class RoadConditions(Conditions):
    road_conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
