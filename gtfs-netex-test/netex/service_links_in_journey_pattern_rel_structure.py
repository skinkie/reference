from dataclasses import dataclass, field
from typing import List
from netex.service_link_in_journey_pattern import ServiceLinkInJourneyPattern
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceLinksInJourneyPatternRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of SERVICE LINKs IN JOURNEY PATTERN.
    """
    class Meta:
        name = "serviceLinksInJourneyPattern_RelStructure"

    service_link_in_journey_pattern: List[ServiceLinkInJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "ServiceLinkInJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
