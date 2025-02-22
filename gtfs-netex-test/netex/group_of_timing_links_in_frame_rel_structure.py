from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .group_of_timing_links import GroupOfTimingLinks

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GroupOfTimingLinksInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "groupOfTimingLinksInFrame_RelStructure"

    group_of_timing_links: list[GroupOfTimingLinks] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfTimingLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
