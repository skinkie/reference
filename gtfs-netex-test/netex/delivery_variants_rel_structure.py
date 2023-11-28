from dataclasses import dataclass, field
from typing import List
from netex.delivery_variant import DeliveryVariant
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DeliveryVariantsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of DELIVERY VARIANTs.
    """
    class Meta:
        name = "deliveryVariants_RelStructure"

    delivery_variant: List[DeliveryVariant] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryVariant",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
