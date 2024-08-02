from dataclasses import dataclass, field
from typing import List

from .stop_place_ref import StopPlaceRef

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class StopPlaceRefsStructure:
    stop_place_ref: List[StopPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_occurs": 1,
        },
    )
