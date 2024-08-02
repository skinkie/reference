from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .abstract_capabilities_structure import AbstractCapabilitiesStructure
from .capability_subscription_policy_structure import CapabilitySubscriptionPolicyStructure
from .filter_by_destination import FilterByDestination
from .filter_by_direction_ref import FilterByDirectionRef
from .filter_by_line_ref import FilterByLineRef
from .filter_by_monitoring_ref import FilterByMonitoringRef
from .monitoring_capability_access_control_structure import MonitoringCapabilityAccessControlStructure
from .stop_monitoring_capability_request_policy_structure import StopMonitoringCapabilityRequestPolicyStructure
from .stop_monitoring_detail_enumeration import StopMonitoringDetailEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopMonitoringServiceCapabilitiesStructure(AbstractCapabilitiesStructure):
    topic_filtering: Optional["StopMonitoringServiceCapabilitiesStructure.TopicFiltering"] = field(
        default=None,
        metadata={
            "name": "TopicFiltering",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_policy: Optional["StopMonitoringServiceCapabilitiesStructure.RequestPolicy"] = field(
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
    access_control: Optional[MonitoringCapabilityAccessControlStructure] = field(
        default=None,
        metadata={
            "name": "AccessControl",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    response_features: Optional["StopMonitoringServiceCapabilitiesStructure.ResponseFeatures"] = field(
        default=None,
        metadata={
            "name": "ResponseFeatures",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class TopicFiltering:
        default_preview_interval: XmlDuration = field(
            default=XmlDuration("PT60M"),
            metadata={
                "name": "DefaultPreviewInterval",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
        by_start_time: Optional[bool] = field(
            default=None,
            metadata={
                "name": "ByStartTime",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_monitoring_ref: FilterByMonitoringRef = field(
            metadata={
                "name": "FilterByMonitoringRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            }
        )
        filter_by_line_ref: FilterByLineRef = field(
            metadata={
                "name": "FilterByLineRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            }
        )
        filter_by_direction_ref: Optional[FilterByDirectionRef] = field(
            default=None,
            metadata={
                "name": "FilterByDirectionRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_destination: Optional[FilterByDestination] = field(
            default=None,
            metadata={
                "name": "FilterByDestination",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_visit_type: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByVisitType",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass(kw_only=True)
    class RequestPolicy(StopMonitoringCapabilityRequestPolicyStructure):
        has_detail_level: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasDetailLevel",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        default_detail_level: Optional[StopMonitoringDetailEnumeration] = field(
            default=None,
            metadata={
                "name": "DefaultDetailLevel",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        has_maximum_visits: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasMaximumVisits",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        has_minimum_visits_per_line: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasMinimumVisitsPerLine",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        has_minimum_visits_per_via: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasMinimumVisitsPerVia",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        has_number_of_onwards_calls: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasNumberOfOnwardsCalls",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        has_number_of_previous_calls: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasNumberOfPreviousCalls",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass(kw_only=True)
    class ResponseFeatures:
        has_line_notices: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasLineNotices",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        has_situations: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasSituations",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
