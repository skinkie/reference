from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.point_of_interest import PointOfInterest

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointsOfInterestInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of POINT OF INTEREST.
    """
    class Meta:
        name = "pointsOfInterestInFrame_RelStructure"

    point_of_interest: List[PointOfInterest] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
