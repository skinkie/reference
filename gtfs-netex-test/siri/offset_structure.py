from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class OffsetStructure:
    distance_from_start: Optional[int] = field(
        default=None,
        metadata={
            "name": "DistanceFromStart",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distance_from_end: Optional[int] = field(
        default=None,
        metadata={
            "name": "DistanceFromEnd",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
