from dataclasses import dataclass, field
from typing import List, Optional

from .error_condition_structure import ErrorConditionStructure
from .extensions_1 import Extensions1
from .participant_ref_structure import ParticipantRefStructure
from .producer_response_structure import ProducerResponseStructure
from .subscription_filter_ref_structure import SubscriptionFilterRefStructure
from .subscription_ref_structure import SubscriptionRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SubscriptionTerminatedNotificationStructure(ProducerResponseStructure):
    subscriber_ref: List[ParticipantRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_filter_ref: List[SubscriptionFilterRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "SubscriptionFilterRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_ref: List[SubscriptionRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "SubscriptionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    errror_condition: Optional[ErrorConditionStructure] = field(
        default=None,
        metadata={
            "name": "ErrrorCondition",
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
