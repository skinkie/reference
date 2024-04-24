from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .group_of_sites import GroupOfSites

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupsOfSitesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "groupsOfSites_RelStructure"

    group_of_sites: List[GroupOfSites] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfSites",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
