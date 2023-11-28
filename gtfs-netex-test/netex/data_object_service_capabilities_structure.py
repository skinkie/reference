from dataclasses import dataclass, field
from typing import Optional
from netex.abstract_capabilities_structure import AbstractCapabilitiesStructure
from netex.data_object_capability_request_policy_structure import DataObjectCapabilityRequestPolicyStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DataObjectServiceCapabilitiesStructure(AbstractCapabilitiesStructure):
    """Type for DATA OBJECT Capabilities.

    This is a stub - needs developing .

    :ivar topic_filtering: Available Filtering Capabilities.
    :ivar request_policy: Available Request Policy capabilities.
    :ivar subscription_policy: Available Subscription Policy
        capabilities.
    :ivar response_features: Available Optional Response capabilities.
    """
    topic_filtering: Optional["DataObjectServiceCapabilitiesStructure.TopicFiltering"] = field(
        default=None,
        metadata={
            "name": "TopicFiltering",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    request_policy: Optional[DataObjectCapabilityRequestPolicyStructure] = field(
        default=None,
        metadata={
            "name": "RequestPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    subscription_policy: Optional["DataObjectServiceCapabilitiesStructure.SubscriptionPolicy"] = field(
        default=None,
        metadata={
            "name": "SubscriptionPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    response_features: Optional[object] = field(
        default=None,
        metadata={
            "name": "ResponseFeatures",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass(unsafe_hash=True, kw_only=True)
    class TopicFiltering:
        """
        :ivar filter_by_frame: Whether results can be filtered by
            VistitType, e.g. arrivals, departures. Default True.
        """
        filter_by_frame: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByFrame",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )

    @dataclass(unsafe_hash=True, kw_only=True)
    class SubscriptionPolicy:
        """
        :ivar has_incremental_updates: Whether incremental updates can
            be specified for updates Default is ' true'.
        """
        has_incremental_updates: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasIncrementalUpdates",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
