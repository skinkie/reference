from dataclasses import dataclass, field
from typing import List
from netex.fare_quota_factor import FareQuotaFactor
from netex.fare_quota_factor_ref import FareQuotaFactorRef
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareQuotaFactorsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of FARE QUOTA FACTOR.
    """
    class Meta:
        name = "fareQuotaFactors_RelStructure"

    fare_quota_factor_ref_or_fare_quota_factor: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareQuotaFactorRef",
                    "type": FareQuotaFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareQuotaFactor",
                    "type": FareQuotaFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
