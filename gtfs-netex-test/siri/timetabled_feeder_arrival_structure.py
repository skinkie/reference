from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from .abstract_feeder_item_structure import AbstractFeederItemStructure
from .extensions_1 import Extensions1
from .interchange_journey_structure import InterchangeJourneyStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TimetabledFeederArrivalStructure(AbstractFeederItemStructure):
    feeder_journey: InterchangeJourneyStructure = field(
        metadata={
            "name": "FeederJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    aimed_arrival_time: XmlDateTime = field(
        metadata={
            "name": "AimedArrivalTime",
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
