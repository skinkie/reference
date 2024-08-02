from dataclasses import dataclass, field
from typing import Optional

from .annotated_stop_point_structure import AnnotatedStopPointStructure
from .extensions_1 import Extensions1
from .line_shape_structure import LineShapeStructure
from .link_projection_structure import LinkProjectionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopPointInPatternStructure(AnnotatedStopPointStructure):
    order: int = field(
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    onward_link_shape: Optional[LineShapeStructure] = field(
        default=None,
        metadata={
            "name": "OnwardLinkShape",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    link_projection_to_next_stop_point: Optional[LinkProjectionStructure] = field(
        default=None,
        metadata={
            "name": "LinkProjectionToNextStopPoint",
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
