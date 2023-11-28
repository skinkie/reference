from dataclasses import dataclass, field
from typing import List
from netex.call import Call
from netex.call_z import CallZ
from netex.dated_call import DatedCall
from netex.dated_call_z import DatedCallZ
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CallsRelStructure(StrictContainmentAggregationStructure):
    """
    CALLs associated with entity.
    """
    class Meta:
        name = "calls_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DatedCall-Z",
                    "type": DatedCallZ,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedCall",
                    "type": DatedCall,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Call-Z",
                    "type": CallZ,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Call",
                    "type": Call,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
