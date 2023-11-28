from dataclasses import dataclass, field
from typing import List
from netex.onward_call import OnwardCall
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OnwardCallsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for List of ONWARD CALLs.

    :ivar onward_call: Onward class after the current call.
    """
    class Meta:
        name = "onwardCalls_RelStructure"

    onward_call: List[OnwardCall] = field(
        default_factory=list,
        metadata={
            "name": "OnwardCall",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
