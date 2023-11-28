from dataclasses import dataclass, field
from typing import List
from netex.fare_demand_factor import FareDemandFactor
from netex.fare_demand_factor_ref import FareDemandFactorRef
from netex.fare_quota_factor import FareQuotaFactor
from netex.fare_quota_factor_ref import FareQuotaFactorRef
from netex.quality_structure_factor import QualityStructureFactor
from netex.quality_structure_factor_ref import QualityStructureFactorRef
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class QualityStructureFactorsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of QUALITY STRUCTURE FACTOR.
    """
    class Meta:
        name = "qualityStructureFactors_RelStructure"

    choice: List[object] = field(
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
                    "name": "FareDemandFactorRef",
                    "type": FareDemandFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorRef",
                    "type": QualityStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareQuotaFactor",
                    "type": FareQuotaFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDemandFactor",
                    "type": FareDemandFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactor",
                    "type": QualityStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
