from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.journey_part import JourneyPart

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPartsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of  JOURNEY PARTs.
    """
    class Meta:
        name = "journeyPartsInFrame_RelStructure"

    journey_part: List[JourneyPart] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
