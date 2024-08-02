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
from .filter_by_connection_link_ref import FilterByConnectionLinkRef
from .filter_by_facility_ref import FilterByFacilityRef
from .filter_by_interchange_ref import FilterByInterchangeRef
from .filter_by_line_ref import FilterByLineRef
from .filter_by_stop_point_ref import FilterByStopPointRef
from .filter_by_vehicle_journey_ref import FilterByVehicleJourneyRef
from .filter_by_vehicle_ref import FilterByVehicleRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SituationExchangeServiceCapabilitiesStructure(AbstractCapabilitiesStructure):
    topic_filtering: Optional["SituationExchangeServiceCapabilitiesStructure.TopicFiltering"] = field(
        default=None,
        metadata={
            "name": "TopicFiltering",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_policy: Optional["SituationExchangeServiceCapabilitiesStructure.RequestPolicy"] = field(
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
    access_control: Optional["SituationExchangeServiceCapabilitiesStructure.AccessControl"] = field(
        default=None,
        metadata={
            "name": "AccessControl",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    response_features: Optional[object] = field(
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
        filter_by_facility_ref: Optional[FilterByFacilityRef] = field(
            default=None,
            metadata={
                "name": "FilterByFacilityRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_location_ref: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByLocationRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
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
        filter_by_mode: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByMode",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_network_ref: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByNetworkRef",
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
        filter_by_stop_point_ref: Optional[FilterByStopPointRef] = field(
            default=None,
            metadata={
                "name": "FilterByStopPointRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_stop_place_ref: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByStopPlaceRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_vehicle_journey_ref: Optional[FilterByVehicleJourneyRef] = field(
            default=None,
            metadata={
                "name": "FilterByVehicleJourneyRef",
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
        filter_by_interchange_ref: Optional[FilterByInterchangeRef] = field(
            default=None,
            metadata={
                "name": "FilterByInterchangeRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_specific_need: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterBySpecificNeed",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_keyword: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByKeyword",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass(kw_only=True)
    class RequestPolicy(CapabilityRequestPolicyStructure):
        has_maximum_number_of_situations: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasMaximumNumberOfSituations",
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
