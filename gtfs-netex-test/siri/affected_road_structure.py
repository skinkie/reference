from dataclasses import dataclass, field
from typing import Optional

from .extensions_1 import Extensions1
from .link_projection_structure import LinkProjectionStructure
from .offset_structure import OffsetStructure
from .roadside_reference_point_linear import RoadsideReferencePointLinear

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AffectedRoadStructure:
    road: Optional[RoadsideReferencePointLinear] = field(
        default=None,
        metadata={
            "name": "Road",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    link_projection: Optional[LinkProjectionStructure] = field(
        default=None,
        metadata={
            "name": "LinkProjection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    offset: Optional[OffsetStructure] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
