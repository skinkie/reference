from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .path_junction import PathJunction
from .site_path_junction import SitePathJunction

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SitePathJunctionsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "sitePathJunctionsInFrame_RelStructure"

    site_path_junction_or_path_junction: List[Union[SitePathJunction, PathJunction]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SitePathJunction",
                    "type": SitePathJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathJunction",
                    "type": PathJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
