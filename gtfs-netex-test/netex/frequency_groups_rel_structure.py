from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .headway_journey_group import HeadwayJourneyGroup
from .headway_journey_group_ref import HeadwayJourneyGroupRef
from .rhythmical_journey_group import RhythmicalJourneyGroup
from .rhythmical_journey_group_ref import RhythmicalJourneyGroupRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FrequencyGroupsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "frequencyGroups_RelStructure"

    headway_journey_group_ref_or_headway_journey_group_or_rhythmical_journey_group_ref_or_rhythmical_journey_group: List[Union[HeadwayJourneyGroupRef, HeadwayJourneyGroup, RhythmicalJourneyGroupRef, RhythmicalJourneyGroup]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "HeadwayJourneyGroupRef",
                    "type": HeadwayJourneyGroupRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HeadwayJourneyGroup",
                    "type": HeadwayJourneyGroup,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RhythmicalJourneyGroupRef",
                    "type": RhythmicalJourneyGroupRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RhythmicalJourneyGroup",
                    "type": RhythmicalJourneyGroup,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
