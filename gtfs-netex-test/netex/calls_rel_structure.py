from dataclasses import dataclass, field
from typing import List

from .call import Call
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CallsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "calls_RelStructure"

    call: List[Call] = field(
        default_factory=list,
        metadata={
            "name": "Call",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
