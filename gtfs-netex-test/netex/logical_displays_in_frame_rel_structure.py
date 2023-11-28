from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.logical_display import LogicalDisplay

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LogicalDisplaysInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of LOGICAL DISPLAY.
    """
    class Meta:
        name = "logicalDisplaysInFrame_RelStructure"

    logical_display: List[LogicalDisplay] = field(
        default_factory=list,
        metadata={
            "name": "LogicalDisplay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
