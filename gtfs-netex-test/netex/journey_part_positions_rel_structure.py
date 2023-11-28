from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.journey_part_position import JourneyPartPosition

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPartPositionsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of JOURNEY PART POSITIONs.
    """
    class Meta:
        name = "journeyPartPositions_RelStructure"

    journey_part_position: List[JourneyPartPosition] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPartPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
