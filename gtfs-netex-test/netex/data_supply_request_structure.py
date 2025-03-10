from dataclasses import dataclass, field
from typing import Optional

from .consumer_request_endpoint_structure import ConsumerRequestEndpointStructure
from .message_ref_structure import MessageRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class DataSupplyRequestStructure(ConsumerRequestEndpointStructure):
    notification_ref: Optional[MessageRefStructure] = field(
        default=None,
        metadata={
            "name": "NotificationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    all_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllData",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
