from dataclasses import dataclass, field
from typing import List
from netex.monitored_call import MonitoredCall
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MonitoredCallsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for List of MONITORED CALLs.
    """
    class Meta:
        name = "monitoredCalls_RelStructure"

    monitored_call: List[MonitoredCall] = field(
        default_factory=list,
        metadata={
            "name": "MonitoredCall",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 2,
        }
    )
