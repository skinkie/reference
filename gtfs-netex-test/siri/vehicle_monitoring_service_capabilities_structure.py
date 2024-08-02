from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .abstract_capabilities_structure import AbstractCapabilitiesStructure
from .capability_access_control_structure import CapabilityAccessControlStructure
from .capability_request_policy_structure import CapabilityRequestPolicyStructure
from .capability_subscription_policy_structure import CapabilitySubscriptionPolicyStructure
from .check_line_ref import CheckLineRef
from .check_operator_ref import CheckOperatorRef
from .extensions_1 import Extensions1
from .filter_by_direction_ref import FilterByDirectionRef
from .filter_by_line_ref import FilterByLineRef
from .filter_by_vehicle_ref import FilterByVehicleRef
from .vehicle_monitoring_detail_enumeration import VehicleMonitoringDetailEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleMonitoringServiceCapabilitiesStructure(AbstractCapabilitiesStructure):
    topic_filtering: Optional["VehicleMonitoringServiceCapabilitiesStructure.TopicFiltering"] = field(
        default=None,
        metadata={
            "name": "TopicFiltering",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_policy: Optional["VehicleMonitoringServiceCapabilitiesStructure.RequestPolicy"] = field(
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
    access_control: Optional["VehicleMonitoringServiceCapabilitiesStructure.AccessControl"] = field(
        default=None,
        metadata={
            "name": "AccessControl",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    response_features: Optional["VehicleMonitoringServiceCapabilitiesStructure.ResponseFeatures"] = field(
        default=None,
        metadata={
            "name": "ResponseFeatures",
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
        default_preview_interval: XmlDuration = field(
            default=XmlDuration("PT60M"),
            metadata={
                "name": "DefaultPreviewInterval",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
        filter_by_vehicle_monitoring_ref: bool = field(
            init=False,
            default=True,
            metadata={
                "name": "FilterByVehicleMonitoringRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
        filter_by_vehicle_ref: Optional[FilterByVehicleRef] = field(
            default=None,
            metadata={
                "name": "FilterByVehicleRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_line_ref: Optional[FilterByLineRef] = field(
            default=None,
            metadata={
                "name": "FilterByLineRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_direction_ref: Optional[FilterByDirectionRef] = field(
            default=None,
            metadata={
                "name": "FilterByDirectionRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass(kw_only=True)
    class RequestPolicy(CapabilityRequestPolicyStructure):
        has_detail_level: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasDetailLevel",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        default_detail_level: Optional[VehicleMonitoringDetailEnumeration] = field(
            default=None,
            metadata={
                "name": "DefaultDetailLevel",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        has_maximum_vehicles: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasMaximumVehicles",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        has_maximum_number_of_calls: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasMaximumNumberOfCalls",
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
    class AccessControl(CapabilityAccessControlStructure):
        check_operator_ref: Optional[CheckOperatorRef] = field(
            default=None,
            metadata={
                "name": "CheckOperatorRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        check_line_ref: Optional[CheckLineRef] = field(
            default=None,
            metadata={
                "name": "CheckLineRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        check_vehicle_monitoring_ref: Optional[bool] = field(
            default=None,
            metadata={
                "name": "CheckVehicleMonitoringRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass(kw_only=True)
    class ResponseFeatures:
        has_location: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasLocation",
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
