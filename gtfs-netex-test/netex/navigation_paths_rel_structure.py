from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.navigation_path import NavigationPath
from netex.navigation_path_ref import NavigationPathRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NavigationPathsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of NAVIGATION PATHs.
    """
    class Meta:
        name = "navigationPaths_RelStructure"

    navigation_path_ref_or_navigation_path: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "NavigationPathRef",
                    "type": NavigationPathRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NavigationPath",
                    "type": NavigationPath,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
