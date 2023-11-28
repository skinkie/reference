from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.group_of_single_journeys import GroupOfSingleJourneys

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupsOfSingleJourneysRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of references to GROUPs OF SINGLE JOURNEYs.
    """
    class Meta:
        name = "groupsOfSingleJourneys_RelStructure"

    group_of_single_journeys: List[GroupOfSingleJourneys] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfSingleJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
