from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.path_junction import PathJunction

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PathJunctionsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of PATH JUNCTIONs.

    :ivar path_junction: A designated path between two PLACEs. May
        include an Ordered sequence of references to PATH LINKS.
    """
    class Meta:
        name = "pathJunctionsInFrame_RelStructure"

    path_junction: List[PathJunction] = field(
        default_factory=list,
        metadata={
            "name": "PathJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
