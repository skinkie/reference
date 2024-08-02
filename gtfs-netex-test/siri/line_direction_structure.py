from dataclasses import dataclass, field
from typing import Optional

from .direction_ref_structure import DirectionRefStructure
from .line_ref_structure import LineRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class LineDirectionStructure:
    line_ref: LineRefStructure = field(
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    direction_ref: Optional[DirectionRefStructure] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
