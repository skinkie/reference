from dataclasses import dataclass, field
from typing import Optional

from .abstract_subscription_structure import AbstractSubscriptionStructure
from .connection_timetable_request import ConnectionTimetableRequest
from .extensions_1 import Extensions1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionTimetableSubscriptionStructure(AbstractSubscriptionStructure):
    connection_timetable_request: ConnectionTimetableRequest = field(
        metadata={
            "name": "ConnectionTimetableRequest",
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
