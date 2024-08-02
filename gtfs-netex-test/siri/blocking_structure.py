from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class BlockingStructure:
    journey_planner: Optional[bool] = field(
        default=None,
        metadata={
            "name": "JourneyPlanner",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    real_time: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RealTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
