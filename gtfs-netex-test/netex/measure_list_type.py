from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class MeasureListType:
    """
    Gml:MeasureListType provides for a list of quantities.
    """
    value: List[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
    uom: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[^: \n\r\t]+",
        }
    )
