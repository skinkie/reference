from dataclasses import dataclass, field

from .service_link_in_journey_pattern import ServiceLinkInJourneyPattern
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ServiceLinksInJourneyPatternRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "serviceLinksInJourneyPattern_RelStructure"

    service_link_in_journey_pattern: list[ServiceLinkInJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "ServiceLinkInJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
