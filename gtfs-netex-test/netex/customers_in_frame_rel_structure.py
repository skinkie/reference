from dataclasses import dataclass, field
from typing import List
from netex.customer import Customer
from netex.frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomersInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of CUSTOMERs.
    """
    class Meta:
        name = "customersInFrame_RelStructure"

    customer: List[Customer] = field(
        default_factory=list,
        metadata={
            "name": "Customer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
