from dataclasses import dataclass, field
from typing import Optional, Union

from .bounding_box_structure import BoundingBoxStructure
from .circular_area_structure import CircularAreaStructure
from .polygon import Polygon

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FlexibleAreaStructure:
    bounding_box_or_circular_area_or_polygon: Optional[Union[BoundingBoxStructure, CircularAreaStructure, Polygon]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BoundingBox",
                    "type": BoundingBoxStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "CircularArea",
                    "type": CircularAreaStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Polygon",
                    "type": Polygon,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
            ),
        },
    )
