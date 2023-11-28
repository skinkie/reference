from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.headway_journey_group import HeadwayJourneyGroup
from netex.rhythmical_journey_group import RhythmicalJourneyGroup

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FrequencyGroupsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of  OURNEY FREQUENCY GROUPs.
    """
    class Meta:
        name = "frequencyGroupsInFrame_RelStructure"

    headway_journey_group_or_rhythmical_journey_group: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "HeadwayJourneyGroup",
                    "type": HeadwayJourneyGroup,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RhythmicalJourneyGroup",
                    "type": RhythmicalJourneyGroup,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
