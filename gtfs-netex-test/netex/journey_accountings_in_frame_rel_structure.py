from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.journey_accounting import JourneyAccounting

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyAccountingsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of VEHICLE TYPEs.
    """
    class Meta:
        name = "journeyAccountingsInFrame_RelStructure"

    journey_accounting: List[JourneyAccounting] = field(
        default_factory=list,
        metadata={
            "name": "JourneyAccounting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
