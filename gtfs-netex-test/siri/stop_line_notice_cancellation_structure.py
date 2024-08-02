from dataclasses import dataclass, field
from typing import Optional

from .abstract_referencing_item_structure import AbstractReferencingItemStructure
from .direction_ref_structure import DirectionRefStructure
from .extensions_1 import Extensions1
from .line_ref_structure import LineRefStructure
from .monitoring_ref_structure import MonitoringRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopLineNoticeCancellationStructure(AbstractReferencingItemStructure):
    monitoring_ref: MonitoringRefStructure = field(
        metadata={
            "name": "MonitoringRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    line_ref: LineRefStructure = field(
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    direction_ref: DirectionRefStructure = field(
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
