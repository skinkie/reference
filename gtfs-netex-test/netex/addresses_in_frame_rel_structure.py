from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.postal_address import PostalAddress
from netex.road_address import RoadAddress

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AddressesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of ADDRESSes.
    """
    class Meta:
        name = "addressesInFrame_RelStructure"

    postal_address_or_road_address: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PostalAddress",
                    "type": PostalAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadAddress",
                    "type": RoadAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
