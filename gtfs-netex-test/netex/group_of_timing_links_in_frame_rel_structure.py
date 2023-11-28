from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.group_of_timing_links import GroupOfTimingLinks

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfTimingLinksInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of GROUP OF TIMING LINKs.
    """
    class Meta:
        name = "groupOfTimingLinksInFrame_RelStructure"

    group_of_timing_links: List[GroupOfTimingLinks] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfTimingLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
