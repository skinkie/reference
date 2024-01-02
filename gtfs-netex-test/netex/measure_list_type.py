from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class MeasureListType:
    value: List[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
    uom: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[^: \n\r\t]+",
        }
    )
