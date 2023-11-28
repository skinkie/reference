from dataclasses import dataclass, field
from typing import List
from netex.access_summary import AccessSummary
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessSummariesRelStructure(StrictContainmentAggregationStructure):
    """
    A collection of one or more ACCESS SUMMARies.
    """
    class Meta:
        name = "accessSummaries_RelStructure"

    access_summary: List[AccessSummary] = field(
        default_factory=list,
        metadata={
            "name": "AccessSummary",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
