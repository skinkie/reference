from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .navigation_path import NavigationPath
from .site_navigation_path import SiteNavigationPath

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NavigationPathsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "navigationPathsInFrame_RelStructure"

    site_navigation_path_or_navigation_path: List[Union[SiteNavigationPath, NavigationPath]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SiteNavigationPath",
                    "type": SiteNavigationPath,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NavigationPath",
                    "type": NavigationPath,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
