from dataclasses import dataclass, field

from .pricing_service import PricingService
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PricingServicesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "pricingServices_RelStructure"

    pricing_service: list[PricingService] = field(
        default_factory=list,
        metadata={
            "name": "PricingService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
