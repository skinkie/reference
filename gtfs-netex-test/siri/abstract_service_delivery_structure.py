from dataclasses import dataclass, field
from typing import List, Optional, Union

from xsdata.models.datatype import XmlDateTime, XmlDuration

from .message_ref_structure import MessageRefStructure
from .participant_ref_structure import ParticipantRefStructure
from .response_structure import ResponseStructure
from .service_delivery_error_condition_structure import ServiceDeliveryErrorConditionStructure
from .status import Status
from .subscription_filter_ref_structure import SubscriptionFilterRefStructure
from .subscription_ref_structure import SubscriptionRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractServiceDeliveryStructure(ResponseStructure):
    request_message_ref_or_subscriber_ref_or_subscription_filter_ref_or_subscription_ref: List[Union[MessageRefStructure, ParticipantRefStructure, SubscriptionFilterRefStructure, SubscriptionRefStructure]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RequestMessageRef",
                    "type": MessageRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "SubscriberRef",
                    "type": ParticipantRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "SubscriptionFilterRef",
                    "type": SubscriptionFilterRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "SubscriptionRef",
                    "type": SubscriptionRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
            "max_occurs": 3,
        },
    )
    delegator_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "DelegatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    error_condition: Optional[ServiceDeliveryErrorConditionStructure] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    valid_until: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ValidUntil",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    shortest_possible_cycle: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ShortestPossibleCycle",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    default_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultLanguage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
