from dataclasses import dataclass, field

from .access_summary import AccessSummary
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AccessSummariesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "accessSummaries_RelStructure"

    access_summary: list[AccessSummary] = field(
        default_factory=list,
        metadata={
            "name": "AccessSummary",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
