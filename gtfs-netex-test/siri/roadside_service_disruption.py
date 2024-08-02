from dataclasses import dataclass, field
from typing import List, Optional

from .extension_type import ExtensionType
from .non_road_event_information import NonRoadEventInformation
from .roadside_service_disruption_type_enum import RoadsideServiceDisruptionTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class RoadsideServiceDisruption(NonRoadEventInformation):
    roadside_service_disruption_type: List[RoadsideServiceDisruptionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "roadsideServiceDisruptionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    roadside_service_disruption_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadsideServiceDisruptionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
