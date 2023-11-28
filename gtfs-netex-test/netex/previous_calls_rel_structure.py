from dataclasses import dataclass, field
from typing import List
from netex.previous_call import PreviousCall
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PreviousCallsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for List of PREVIOUS CALLs.
    """
    class Meta:
        name = "previousCalls_RelStructure"

    previous_call: List[PreviousCall] = field(
        default_factory=list,
        metadata={
            "name": "PreviousCall",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
