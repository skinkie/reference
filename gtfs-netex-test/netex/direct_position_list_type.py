from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(slots=True, kw_only=True)
class DirectPositionListType:
    value: list[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        },
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
