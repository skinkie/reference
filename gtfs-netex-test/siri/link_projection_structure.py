from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_projection import AbstractProjection
from .point_projection import PointProjection

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class LinkProjectionStructure(AbstractProjection):
    line: Optional["LinkProjectionStructure.Line"] = field(
        default=None,
        metadata={
            "name": "Line",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )

    @dataclass(kw_only=True)
    class Line:
        point_projection: List[PointProjection] = field(
            default_factory=list,
            metadata={
                "name": "PointProjection",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/ifopt",
                "min_occurs": 2,
            },
        )
