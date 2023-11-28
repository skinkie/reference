from dataclasses import dataclass, field
from typing import List
from netex.data_object_delivery import DataObjectDelivery

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DeliveriesStructure:
    """
    Type for Deliveries for  Service.

    :ivar data_object_delivery: Delivery for Stop Event service.
    """
    data_object_delivery: List[DataObjectDelivery] = field(
        default_factory=list,
        metadata={
            "name": "DataObjectDelivery",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
