from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.relief_opportunity import ReliefOpportunity
from netex.relief_opportunity_ref import ReliefOpportunityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ReliefOpportunitiesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of RELIEF OPPORTUNITies.
    """
    class Meta:
        name = "reliefOpportunities_RelStructure"

    relief_opportunity_ref_or_relief_opportunity: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ReliefOpportunityRef",
                    "type": ReliefOpportunityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefOpportunity",
                    "type": ReliefOpportunity,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
