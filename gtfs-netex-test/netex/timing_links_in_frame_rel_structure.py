from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.timing_link import TimingLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimingLinksInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of TIMING LINK.
    """
    class Meta:
        name = "timingLinksInFrame_RelStructure"

    timing_link: List[TimingLink] = field(
        default_factory=list,
        metadata={
            "name": "TimingLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
