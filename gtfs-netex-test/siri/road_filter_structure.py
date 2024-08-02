from dataclasses import dataclass, field
from typing import Optional

from .direction_enum import DirectionEnum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RoadFilterStructure:
    road_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "max_length": 1024,
        },
    )
    direction_bound: Optional[DirectionEnum] = field(
        default=None,
        metadata={
            "name": "directionBound",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reference_point_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "referencePointIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "max_length": 1024,
        },
    )
