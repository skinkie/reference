from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.destination_display import DestinationDisplay

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DestinationDisplaysInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of DESTINATION DISPLAY.
    """
    class Meta:
        name = "destinationDisplaysInFrame_RelStructure"

    destination_display: List[DestinationDisplay] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
