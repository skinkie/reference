from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .topographic_place import TopographicPlace
from .topographic_place_ref import TopographicPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TopographicPlacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "topographicPlaces_RelStructure"

    topographic_place_ref: list[TopographicPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    topographic_place: list[TopographicPlace] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
