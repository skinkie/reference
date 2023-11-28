from dataclasses import dataclass, field
from typing import Optional
from netex.direction_ref import DirectionRef
from netex.external_object_ref_structure import ExternalObjectRefStructure
from netex.flexible_line_ref import FlexibleLineRef
from netex.line_ref import LineRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LineInDirectionRefStructure:
    """
    Type for a Reference to a LINE in a specific DIRECTION.

    :ivar flexible_line_ref_or_line_ref:
    :ivar direction_ref:
    :ivar external_line_ref: Alternative  LINE Reference  for AVMS
        system.
    :ivar external_direction_ref: Alternative DIRECTION Reference  for
        AVMS system.
    """
    class Meta:
        name = "LineInDirectionRef_Structure"

    flexible_line_ref_or_line_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    direction_ref: Optional[DirectionRef] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    external_line_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    external_direction_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalDirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
