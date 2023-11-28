from dataclasses import dataclass, field
from typing import List
from netex.dated_call import DatedCall
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DatedCallsRelStructure(StrictContainmentAggregationStructure):
    """
    DatedCALLs associated with entity.

    :ivar dated_call: A CALL that is part of a DATED JOURNEY and so
        takes place on a specified date.
    """
    class Meta:
        name = "datedCalls_RelStructure"

    dated_call: List[DatedCall] = field(
        default_factory=list,
        metadata={
            "name": "DatedCall",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 2,
        }
    )
