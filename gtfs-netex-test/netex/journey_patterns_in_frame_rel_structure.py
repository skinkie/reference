from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.dead_run_journey_pattern import DeadRunJourneyPattern
from netex.journey_pattern_view import JourneyPatternView
from netex.section_in_sequence_versioned_child_structure import JourneyPattern
from netex.service_journey_pattern import ServiceJourneyPattern

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPatternsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of JOURNEY PATTERNs.
    """
    class Meta:
        name = "journeyPatternsInFrame_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyPattern",
                    "type": ServiceJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPattern",
                    "type": DeadRunJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPattern",
                    "type": JourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternView",
                    "type": JourneyPatternView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
