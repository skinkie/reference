from dataclasses import dataclass, field
from typing import List, Optional
from netex.abstract_surface_type import AbstractSurfaceType
from netex.exterior import Exterior
from netex.interior import Interior

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class PolygonType(AbstractSurfaceType):
    exterior: Optional[Exterior] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    interior: List[Interior] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
