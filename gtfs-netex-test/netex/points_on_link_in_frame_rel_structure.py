from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.point_on_link import PointOnLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointsOnLinkInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of POINTs ON LINK.
    """
    class Meta:
        name = "pointsOnLinkInFrame_RelStructure"

    point_on_link: List[PointOnLink] = field(
        default_factory=list,
        metadata={
            "name": "PointOnLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
