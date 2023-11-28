from dataclasses import dataclass, field
from typing import List
from netex.fare_demand_factor import FareDemandFactor
from netex.fare_demand_factor_ref import FareDemandFactorRef
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareDemandFactorsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of FARE DEMAND FACTOR.
    """
    class Meta:
        name = "fareDemandFactors_RelStructure"

    fare_demand_factor_ref_or_fare_demand_factor: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareDemandFactorRef",
                    "type": FareDemandFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDemandFactor",
                    "type": FareDemandFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
