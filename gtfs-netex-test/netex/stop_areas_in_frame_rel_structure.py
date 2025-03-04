from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .stop_area import StopArea

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class StopAreasInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "stopAreasInFrame_RelStructure"

    stop_area: list[StopArea] = field(
        default_factory=list,
        metadata={
            "name": "StopArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
