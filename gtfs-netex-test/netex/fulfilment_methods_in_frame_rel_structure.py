from dataclasses import dataclass, field
from typing import List
from netex.frame_containment_structure import FrameContainmentStructure
from netex.fulfilment_method import FulfilmentMethod

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FulfilmentMethodsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of FULFILMENT METHOD.
    """
    class Meta:
        name = "fulfilmentMethodsInFrame_RelStructure"

    fulfilment_method: List[FulfilmentMethod] = field(
        default_factory=list,
        metadata={
            "name": "FulfilmentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
