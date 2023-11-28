from dataclasses import dataclass, field
from typing import List
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from netex.usage_parameter_price_ref import UsageParameterPriceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UsageParameterPriceRefsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of USAGE PARAMETER PRICEs.
    """
    class Meta:
        name = "usageParameterPriceRefs_RelStructure"

    usage_parameter_price_ref: List[UsageParameterPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameterPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
