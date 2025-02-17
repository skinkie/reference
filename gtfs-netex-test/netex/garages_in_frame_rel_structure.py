from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .garage import Garage

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GaragesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "garagesInFrame_RelStructure"

    garage: list[Garage] = field(
        default_factory=list,
        metadata={
            "name": "Garage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
