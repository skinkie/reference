from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.journey_part_couple import JourneyPartCouple

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPartCouplesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of  JOURNEY PART COUPLEs.
    """
    class Meta:
        name = "journeyPartCouplesInFrame_RelStructure"

    journey_part_couple: List[JourneyPartCouple] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPartCouple",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
