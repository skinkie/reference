from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.submode import Submode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SubmodesRelStructure(ContainmentAggregationStructure):
    """
    SUBMODEs  associated with entity.
    """
    class Meta:
        name = "submodes_RelStructure"

    submode: List[Submode] = field(
        default_factory=list,
        metadata={
            "name": "Submode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
