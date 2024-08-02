from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_item_structure import AbstractItemStructure
from .direction_ref_structure import DirectionRefStructure
from .line_ref import LineRef
from .natural_language_string_structure import NaturalLanguageStringStructure
from .service_exception_enumeration import ServiceExceptionEnumeration
from .situation_simple_ref_structure import SituationSimpleRefStructure
from .stop_point_ref import StopPointRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ServiceExceptionStructure(AbstractItemStructure):
    line_ref: Optional[LineRef] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    direction_ref: Optional[DirectionRefStructure] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_point_ref: Optional[StopPointRef] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    service_status: Optional[ServiceExceptionEnumeration] = field(
        default=None,
        metadata={
            "name": "ServiceStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    notice: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Notice",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_ref: Optional[SituationSimpleRefStructure] = field(
        default=None,
        metadata={
            "name": "SituationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
