from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_identified_item_structure import AbstractIdentifiedItemStructure
from .delivery_variant_structure import DeliveryVariantStructure
from .direction_ref_structure import DirectionRefStructure
from .extensions_1 import Extensions1
from .line_ref_structure import LineRefStructure
from .monitoring_ref_structure import MonitoringRefStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .situation_ref import SituationRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopLineNoticeStructure(AbstractIdentifiedItemStructure):
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
    published_line_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "PublishedLineName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_note: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "LineNote",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delivery_variant: List[DeliveryVariantStructure] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryVariant",
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
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
