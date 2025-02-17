from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .group_of_sites import GroupOfSites

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GroupsOfSitesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "groupsOfSites_RelStructure"

    group_of_sites: list[GroupOfSites] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfSites",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
