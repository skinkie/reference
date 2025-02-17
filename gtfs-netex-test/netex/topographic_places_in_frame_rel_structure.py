from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .topographic_place import TopographicPlace

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TopographicPlacesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "topographicPlacesInFrame_RelStructure"

    topographic_place: list[TopographicPlace] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
