from dataclasses import dataclass, field
from typing import Optional

from .abstract_capabilities_structure import AbstractCapabilitiesStructure
from .capability_request_policy_structure import CapabilityRequestPolicyStructure
from .capability_subscription_policy_structure import CapabilitySubscriptionPolicyStructure
from .connection_capability_access_control_structure import ConnectionCapabilityAccessControlStructure
from .extensions_1 import Extensions1
from .filter_by_connection_link_ref import FilterByConnectionLinkRef
from .filter_by_line_ref import FilterByLineRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionTimetableServiceCapabilitiesStructure(AbstractCapabilitiesStructure):
    topic_filtering: Optional["ConnectionTimetableServiceCapabilitiesStructure.TopicFiltering"] = field(
        default=None,
        metadata={
            "name": "TopicFiltering",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_policy: Optional["ConnectionTimetableServiceCapabilitiesStructure.RequestPolicy"] = field(
        default=None,
        metadata={
            "name": "RequestPolicy",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_policy: Optional[CapabilitySubscriptionPolicyStructure] = field(
        default=None,
        metadata={
            "name": "SubscriptionPolicy",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    access_control: Optional[ConnectionCapabilityAccessControlStructure] = field(
        default=None,
        metadata={
            "name": "AccessControl",
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

    @dataclass(kw_only=True)
    class TopicFiltering:
        filter_by_line_ref: FilterByLineRef = field(
            metadata={
                "name": "FilterByLineRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            }
        )
        filter_by_connection_link_ref: FilterByConnectionLinkRef = field(
            metadata={
                "name": "FilterByConnectionLinkRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class RequestPolicy(CapabilityRequestPolicyStructure):
        foreign_journeys_only: Optional[bool] = field(
            default=None,
            metadata={
                "name": "ForeignJourneysOnly",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
