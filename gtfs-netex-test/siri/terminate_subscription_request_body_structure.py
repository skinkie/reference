from dataclasses import dataclass, field
from typing import List, Optional, Union

from .empty_type import EmptyType
from .participant_ref_structure import ParticipantRefStructure
from .subscription_qualifier_structure import SubscriptionQualifierStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TerminateSubscriptionRequestBodyStructure:
    subscriber_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    all_or_subscription_ref: List[Union[EmptyType, SubscriptionQualifierStructure]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "All",
                    "type": EmptyType,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "SubscriptionRef",
                    "type": SubscriptionQualifierStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
