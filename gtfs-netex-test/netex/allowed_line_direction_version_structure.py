from dataclasses import dataclass, field
from typing import Optional, Union

from .direction_ref import DirectionRef
from .entity_in_version_structure import DataManagedObjectStructure
from .flexible_line_ref import FlexibleLineRef
from .line_ref import LineRef
from .presentation_structure import PresentationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AllowedLineDirectionVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "AllowedLineDirection_VersionStructure"

    line_ref: Optional[Union[FlexibleLineRef, LineRef]] = field(
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
        },
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
        },
    )
