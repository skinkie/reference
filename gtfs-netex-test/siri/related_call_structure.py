from dataclasses import dataclass, field
from typing import Optional

from .abstract_call_structure import AbstractCallStructure
from .aimed_arrival_time import AimedArrivalTime
from .aimed_departure_time import AimedDepartureTime

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RelatedCallStructure(AbstractCallStructure):
    aimed_departure_time: Optional[AimedDepartureTime] = field(
        default=None,
        metadata={
            "name": "AimedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_arrival_time: Optional[AimedArrivalTime] = field(
        default=None,
        metadata={
            "name": "AimedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
