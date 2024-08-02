from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .occupancy_view_version_structure import OccupancyViewVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OccupancyViewInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "OccupancyViewInFrame_RelStructure"

    occupancy_view: OccupancyViewVersionStructure = field(
        metadata={
            "name": "OccupancyView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
