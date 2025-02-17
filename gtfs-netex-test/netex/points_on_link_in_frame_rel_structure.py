from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .point_on_link import PointOnLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PointsOnLinkInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "pointsOnLinkInFrame_RelStructure"

    point_on_link: list[PointOnLink] = field(
        default_factory=list,
        metadata={
            "name": "PointOnLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
