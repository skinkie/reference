from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .abstract_subscription_structure import AbstractSubscriptionStructure
from .extensions_1 import Extensions1
from .stop_timetable_request import StopTimetableRequest

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopTimetableSubscriptionStructure(AbstractSubscriptionStructure):
    stop_timetable_request: StopTimetableRequest = field(
        metadata={
            "name": "StopTimetableRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    incremental_updates: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncrementalUpdates",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    change_before_updates: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ChangeBeforeUpdates",
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
