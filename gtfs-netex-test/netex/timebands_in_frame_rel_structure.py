from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.timeband import Timeband

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimebandsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of TIME BANDs.
    """
    class Meta:
        name = "timebandsInFrame_RelStructure"

    timeband: List[Timeband] = field(
        default_factory=list,
        metadata={
            "name": "Timeband",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
