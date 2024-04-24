from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .contract import Contract

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ContractsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "contractsInFrame_RelStructure"

    contract: List[Contract] = field(
        default_factory=list,
        metadata={
            "name": "Contract",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
