from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.relief_opportunity import ReliefOpportunity

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ReliefOpportunitiesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of RELIEF OPPORTUNITies.
    """
    class Meta:
        name = "reliefOpportunitiesInFrame_RelStructure"

    relief_opportunity: List[ReliefOpportunity] = field(
        default_factory=list,
        metadata={
            "name": "ReliefOpportunity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
