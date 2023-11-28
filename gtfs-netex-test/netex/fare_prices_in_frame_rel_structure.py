from dataclasses import dataclass, field
from typing import List
from netex.cell_versioned_child_structure import PriceGroup
from netex.frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FarePricesInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of FARE Prices.
    """
    class Meta:
        name = "farePricesInFrame_RelStructure"

    price_group: List[PriceGroup] = field(
        default_factory=list,
        metadata={
            "name": "PriceGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
