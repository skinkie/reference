from dataclasses import dataclass, field
from typing import List

from .fare_contract_entries_rel_structure import SalesTransaction
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesTransactionsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "salesTransactionsInFrame_RelStructure"

    sales_transaction: List[SalesTransaction] = field(
        default_factory=list,
        metadata={
            "name": "SalesTransaction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
