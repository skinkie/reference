from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.online_service import OnlineService

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OnlineServicesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of MOBILITY SERVICEs.
    """
    class Meta:
        name = "onlineServices_RelStructure"

    online_service: List[OnlineService] = field(
        default_factory=list,
        metadata={
            "name": "OnlineService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
