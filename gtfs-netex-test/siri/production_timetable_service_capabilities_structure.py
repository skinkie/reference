from dataclasses import dataclass, field
from typing import Optional

from .abstract_capabilities_structure import AbstractCapabilitiesStructure
from .capability_request_policy_structure import CapabilityRequestPolicyStructure
from .connection_capability_access_control_structure import ConnectionCapabilityAccessControlStructure
from .extensions_1 import Extensions1
from .filter_by_line_ref import FilterByLineRef
from .filter_by_operator_ref import FilterByOperatorRef
from .filter_by_product_category_ref import FilterByProductCategoryRef
from .filter_by_stop_point_ref import FilterByStopPointRef
from .filter_by_validity_period import FilterByValidityPeriod
from .filter_by_vehicle_mode import FilterByVehicleMode

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ProductionTimetableServiceCapabilitiesStructure(AbstractCapabilitiesStructure):
    topic_filtering: Optional["ProductionTimetableServiceCapabilitiesStructure.TopicFiltering"] = field(
        default=None,
        metadata={
            "name": "TopicFiltering",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_policy: Optional[CapabilityRequestPolicyStructure] = field(
        default=None,
        metadata={
            "name": "RequestPolicy",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_policy: Optional["ProductionTimetableServiceCapabilitiesStructure.SubscriptionPolicy"] = field(
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
        filter_by_validity_period: FilterByValidityPeriod = field(
            metadata={
                "name": "FilterByValidityPeriod",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            }
        )
        filter_by_operator_ref: FilterByOperatorRef = field(
            metadata={
                "name": "FilterByOperatorRef",
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
        filter_by_vehicle_mode: Optional[FilterByVehicleMode] = field(
            default=None,
            metadata={
                "name": "FilterByVehicleMode",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_product_category_ref: Optional[FilterByProductCategoryRef] = field(
            default=None,
            metadata={
                "name": "FilterByProductCategoryRef",
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
        filter_by_version_ref: bool = field(
            default=True,
            metadata={
                "name": "FilterByVersionRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )

    @dataclass(kw_only=True)
    class SubscriptionPolicy:
        has_incremental_updates: bool = field(
            default=True,
            metadata={
                "name": "HasIncrementalUpdates",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
