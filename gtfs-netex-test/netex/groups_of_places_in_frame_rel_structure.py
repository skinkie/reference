from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.group_of_places import GroupOfPlaces

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupsOfPlacesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of GROUP OF PLACEs.
    """
    class Meta:
        name = "groupsOfPlacesInFrame_RelStructure"

    group_of_places: List[GroupOfPlaces] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
