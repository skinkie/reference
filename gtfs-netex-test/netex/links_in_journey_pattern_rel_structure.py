from dataclasses import dataclass, field
from typing import List
from netex.service_link_in_journey_pattern import ServiceLinkInJourneyPattern
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from netex.timing_link_in_journey_pattern import TimingLinkInJourneyPattern

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LinksInJourneyPatternRelStructure(StrictContainmentAggregationStructure):
    """
    Type for LINK IN JOURNEY PATTERN.
    """
    class Meta:
        name = "linksInJourneyPattern_RelStructure"

    service_link_in_journey_pattern_or_timing_link_in_journey_pattern: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceLinkInJourneyPattern",
                    "type": ServiceLinkInJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingLinkInJourneyPattern",
                    "type": TimingLinkInJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
