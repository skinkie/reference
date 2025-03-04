from dataclasses import dataclass, field

from .abstract_subscription_request_structure import AbstractSubscriptionRequestStructure
from .data_object_subscription_request import DataObjectSubscriptionRequest

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class SubscriptionRequestStructure(AbstractSubscriptionRequestStructure):
    data_object_subscription_request: list[DataObjectSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "DataObjectSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
