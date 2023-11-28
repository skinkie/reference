from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.group_of_operators import GroupOfOperators

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupsOfOperatorsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of GROUP OF OPERATORs.
    """
    class Meta:
        name = "groupsOfOperatorsInFrame_RelStructure"

    group_of_operators: List[GroupOfOperators] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfOperators",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
