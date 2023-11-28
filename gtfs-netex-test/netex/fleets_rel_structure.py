from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.fleet import Fleet

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FleetsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of  FLEETs.
    """
    class Meta:
        name = "fleets_RelStructure"

    fleet: List[Fleet] = field(
        default_factory=list,
        metadata={
            "name": "Fleet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
