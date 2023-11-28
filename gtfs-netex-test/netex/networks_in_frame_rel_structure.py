from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.network import Network

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NetworksInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of NETWORKs.
    """
    class Meta:
        name = "networksInFrame_RelStructure"

    network: List[Network] = field(
        default_factory=list,
        metadata={
            "name": "Network",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
