from dataclasses import dataclass, field
from typing import List
from netex.frame_containment_structure import FrameContainmentStructure
from netex.sales_transaction import SalesTransaction

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesTransactionsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of SALES TRANSACTIONs.
    """
    class Meta:
        name = "salesTransactionsInFrame_RelStructure"

    sales_transaction: List[SalesTransaction] = field(
        default_factory=list,
        metadata={
            "name": "SalesTransaction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
