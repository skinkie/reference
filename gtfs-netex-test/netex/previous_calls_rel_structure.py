from dataclasses import dataclass, field

from .previous_call import PreviousCall
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PreviousCallsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "previousCalls_RelStructure"

    previous_call: list[PreviousCall] = field(
        default_factory=list,
        metadata={
            "name": "PreviousCall",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
