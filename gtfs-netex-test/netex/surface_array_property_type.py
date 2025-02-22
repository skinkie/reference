from dataclasses import dataclass, field

from .polygon import Polygon

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(slots=True, kw_only=True)
class SurfaceArrayPropertyType:
    polygon: list[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
