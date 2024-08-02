from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .occupancy_view_ref_structure import OccupancyViewRefStructure
from .occupancy_view_version_structure import OccupancyViewVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OccupancyViewRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "OccupancyView_RelStructure"

    occupancy_view_or_occupancy_view_ref: List[Union[OccupancyViewVersionStructure, OccupancyViewRefStructure]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OccupancyView",
                    "type": OccupancyViewVersionStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OccupancyViewRef",
                    "type": OccupancyViewRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
