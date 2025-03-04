from dataclasses import dataclass, field

from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .topographic_place_descriptor_versioned_child_structure import TopographicPlaceDescriptorVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TopographicPlaceDescriptorsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "topographicPlaceDescriptors_RelStructure"

    topographic_place_descriptor: list[TopographicPlaceDescriptorVersionedChildStructure] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlaceDescriptor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
