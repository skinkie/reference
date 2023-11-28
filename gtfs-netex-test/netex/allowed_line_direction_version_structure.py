from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.direction_ref import DirectionRef
from netex.flexible_line_ref import FlexibleLineRef
from netex.line_ref import LineRef
from netex.presentation_structure import PresentationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AllowedLineDirectionVersionStructure(DataManagedObjectStructure):
    """
    Type for an ALLOWED LINE DIRECTION.

    :ivar flexible_line_ref_or_line_ref:
    :ivar direction_ref:
    :ivar presentation: Pesentation to use for DIRECTION. +v1.1..
    """
    class Meta:
        name = "AllowedLineDirection_VersionStructure"

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
    direction_ref: DirectionRef = field(
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    presentation: Optional[PresentationStructure] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
