from dataclasses import dataclass, field
from typing import List, Optional
from netex.authenticated_request_structure import AuthenticatedRequestStructure
from netex.empty_type_1 import EmptyType1
from netex.extensions_1 import Extensions1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class TerminateSubscriptionRequestStructure(AuthenticatedRequestStructure):
    """
    Type for request to terminate a subscription or subscriptions.

    :ivar address: Address to which response is to be sent. This may
        also be determined from RequestorRef and preconfigured data.
    :ivar requestor_ref:
    :ivar message_identifier: Arbitrary unique identifier that can be
        used to reference this message in subsequent interactions.
    :ivar delegator_address: Address of original Consumer, i.e.
        requesting system to which delegating response is to be
        returned. +SIRI 2.0
    :ivar delegator_ref: Identifier of delegating system that originated
        message. +SIRI 2.0
    :ivar subscriber_ref: Participant identifier of Subscriber.
        Subscription ref will be unique within this.
    :ivar all_or_subscription_ref:
    :ivar extensions:
    """
    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    requestor_ref: str = field(
        metadata={
            "name": "RequestorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    message_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "MessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    delegator_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    delegator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    subscriber_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    all_or_subscription_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "All",
                    "type": EmptyType1,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "SubscriptionRef",
                    "type": str,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
