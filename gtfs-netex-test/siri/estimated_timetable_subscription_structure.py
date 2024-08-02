from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .abstract_subscription_structure import AbstractSubscriptionStructure
from .estimated_timetable_request import EstimatedTimetableRequest
from .extensions_1 import Extensions1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class EstimatedTimetableSubscriptionStructure(AbstractSubscriptionStructure):
    estimated_timetable_request: EstimatedTimetableRequest = field(
        metadata={
            "name": "EstimatedTimetableRequest",
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
    skip_recorded_call_updates: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SkipRecordedCallUpdates",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    include_only_recorded_call_updates: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeOnlyRecordedCallUpdates",
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
