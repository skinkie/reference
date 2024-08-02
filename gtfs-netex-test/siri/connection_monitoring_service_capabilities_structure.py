from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .abstract_capabilities_structure import AbstractCapabilitiesStructure
from .capability_request_policy_structure import CapabilityRequestPolicyStructure
from .capability_subscription_policy_structure import CapabilitySubscriptionPolicyStructure
from .connection_capability_access_control_structure import ConnectionCapabilityAccessControlStructure
from .extensions_1 import Extensions1
from .filter_by_connection_link_ref import FilterByConnectionLinkRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionMonitoringServiceCapabilitiesStructure(AbstractCapabilitiesStructure):
    topic_filtering: Optional["ConnectionMonitoringServiceCapabilitiesStructure.TopicFiltering"] = field(
        default=None,
        metadata={
            "name": "TopicFiltering",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_policy: Optional["ConnectionMonitoringServiceCapabilitiesStructure.RequestPolicy"] = field(
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
        default_preview_interval: Optional[XmlDuration] = field(
            default=None,
            metadata={
                "name": "DefaultPreviewInterval",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_connection_link_ref: Optional[FilterByConnectionLinkRef] = field(
            default=None,
            metadata={
                "name": "FilterByConnectionLinkRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_journey: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByJourney",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_time: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByTime",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
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
