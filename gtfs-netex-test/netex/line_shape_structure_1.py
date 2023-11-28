from dataclasses import dataclass, field
from typing import List
from netex.location_structure_1 import LocationStructure1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class LineShapeStructure1:
    """
    Defines a line shape +SIRI v2.0.

    :ivar point: A geospatial point. +SIRI v2.0 .
    """
    class Meta:
        name = "LineShapeStructure"

    point: List[LocationStructure1] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 2,
        }
    )
