from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_required_identified_item_structure import AbstractRequiredIdentifiedItemStructure
from .extensions_1 import Extensions1
from .monitoring_ref_structure import MonitoringRefStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .situation_ref import SituationRef
from .stop_point_ref import StopPointRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopNoticeStructure(AbstractRequiredIdentifiedItemStructure):
    monitoring_ref: MonitoringRefStructure = field(
        metadata={
            "name": "MonitoringRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    stop_point_ref: Optional[StopPointRef] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_ref: List[SituationRef] = field(
        default_factory=list,
        metadata={
            "name": "SituationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_note: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopNote",
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
