from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.navigation_path import NavigationPath

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NavigationPathsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of NAVIGATION PATHs.

    :ivar navigation_path: A designated path between two PLACEs. May
        include an Ordered sequence of references to PATH LINKS.
    """
    class Meta:
        name = "navigationPathsInFrame_RelStructure"

    navigation_path: List[NavigationPath] = field(
        default_factory=list,
        metadata={
            "name": "NavigationPath",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
