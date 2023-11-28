from dataclasses import dataclass, field
from typing import List
from netex.pricing_service import PricingService
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PricingServicesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for containment in frame of FARE DYNAMIC PRICING SERVICEs.
    """
    class Meta:
        name = "pricingServices_RelStructure"

    pricing_service: List[PricingService] = field(
        default_factory=list,
        metadata={
            "name": "PricingService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
