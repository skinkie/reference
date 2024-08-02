from dataclasses import dataclass, field
from typing import List

from .abstract_projection import AbstractProjection
from .point_projection import PointProjection

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class ZoneProjectionStructure(AbstractProjection):
    boundary: List["ZoneProjectionStructure.Boundary"] = field(
        default_factory=list,
        metadata={
            "name": "Boundary",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class Boundary:
        point_projection: List[PointProjection] = field(
            default_factory=list,
            metadata={
                "name": "PointProjection",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/ifopt",
                "min_occurs": 3,
            },
        )
