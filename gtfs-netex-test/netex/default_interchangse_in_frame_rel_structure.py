from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.default_interchange import DefaultInterchange

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DefaultInterchangseInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of  DEFAULT INTERCHANGEs.
    """
    class Meta:
        name = "defaultInterchangseInFrame_RelStructure"

    default_interchange: List[DefaultInterchange] = field(
        default_factory=list,
        metadata={
            "name": "DefaultInterchange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
