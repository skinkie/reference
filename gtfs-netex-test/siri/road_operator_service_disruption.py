from dataclasses import dataclass, field
from typing import List, Optional

from .extension_type import ExtensionType
from .non_road_event_information import NonRoadEventInformation
from .road_operator_service_disruption_type_enum import RoadOperatorServiceDisruptionTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class RoadOperatorServiceDisruption(NonRoadEventInformation):
    road_operator_service_disruption_type: List[RoadOperatorServiceDisruptionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "roadOperatorServiceDisruptionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    road_operator_service_disruption_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadOperatorServiceDisruptionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
