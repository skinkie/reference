from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from .multilingual_string import MultilingualString
from .network_frame_request_policy_structure import NetworkFrameRequestPolicyStructure
from .network_frame_subscription_policy_structure import NetworkFrameSubscriptionPolicyStructure
from .network_frame_topic_structure import NetworkFrameTopicStructure
from .participant_ref import ParticipantRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PublicationRequestStructure:
    request_timestamp: XmlDateTime = field(
        metadata={
            "name": "RequestTimestamp",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    participant_ref: Optional[ParticipantRef] = field(
        default=None,
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    topics: Optional["PublicationRequestStructure.Topics"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    request_policy: Optional[NetworkFrameRequestPolicyStructure] = field(
        default=None,
        metadata={
            "name": "RequestPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    subscription_policy: Optional[NetworkFrameSubscriptionPolicyStructure] = field(
        default=None,
        metadata={
            "name": "SubscriptionPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    version: str = field(
        default="1.0",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass(slots=True, kw_only=True)
    class Topics:
        network_frame_topic: list[NetworkFrameTopicStructure] = field(
            default_factory=list,
            metadata={
                "name": "NetworkFrameTopic",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )
